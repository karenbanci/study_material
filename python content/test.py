from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import random


class LayerType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3


class MultiLinkNode(ABC):
    """
    This is an abstract base class that will be the starting point for our eventual FFBPNeurode class.
    """

    class Side(Enum):
        """
        This is an Enum subclass of MultiLinkNode with elements UPSTREAM and DOWNSTREAM.
        We will use these terms to identify relationships between neurodes
        """
        UPSTREAM = 1
        DOWNSTREAM = 2

    def __init__(self):
        """
        The keys will be the two elements of the Side enum.
        The values will initially be set to zero.
        We will use this as a binary encoding to keep track of
        which neighboring nodes have indicated that they have information available
        """
        self._reporting_nodes = {MultiLinkNode.Side.UPSTREAM: 0, MultiLinkNode.Side.DOWNSTREAM: 0}
        self._reference_value = {MultiLinkNode.Side.UPSTREAM: 0, MultiLinkNode.Side.DOWNSTREAM: 0}
        self._neighbors = {MultiLinkNode.Side.UPSTREAM: [], MultiLinkNode.Side.DOWNSTREAM: []}

    def __str__(self):
        """
        Overload this function to print out a representation of the node in context.
        """
        string = ""
        for upstream_neighbor in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            string += "\n upstream: " + str(id(upstream_neighbor))

        string += "\n self: " + str(id(self))

        for downstream_neighbor in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            string += "\n downstream: " + str(id(downstream_neighbor))

        return string

    @abstractmethod
    def _process_new_neighbor(self, node, side):
        """
        This is an abstract method that takes a node and a Side enum as parameters.
        """
        pass

    def reset_neighbors(self, nodes, side):
        # Copy the nodes parameter into the appropriate entry of self._neighbors.
        self._neighbors[side] = nodes.copy()

        # Call _process_new_neighbor() for each node
        for node in nodes:
            self._process_new_neighbor(node, side)

        self._reference_value[side] = (1 << len(self._neighbors[side])) - 1
        self._reporting_nodes[side] = 0

    @property
    def neighbors(self):
        return self._neighbors


class Neurode(MultiLinkNode):
    """
    This class is inherited from and implements MultiLinkNode.
    """

    def __init__(self, node_type, learning_rate=.05):
        self._value = 0
        self._node_type = node_type
        self._learning_rate = learning_rate
        self._weights = dict()
        super().__init__()

    def _process_new_neighbor(self, node, side):
        """
        This method will be called when any new neighbors are added,
        but we really are only concerned with upstream neighbors
        """
        # When an upstream neighbor is added, the node reference
        # will be added as a key to the self._weights dictionary
        if side is MultiLinkNode.Side.UPSTREAM:
            #  The value related to this key should be a randomly generated float between 0 and 1
            self._weights[node] = random.random()

    def _check_in(self, node, side):
        """
        This method will be called whenever the node learns
        that a neighboring node has information available.
        :return True if every node has checked in reporting_nodes
        """
        # Find the node's index in self._neighbors.
        index_node = self._neighbors[side].index(node)

        # Use this index to update self._reporting_nodes to reflect that this node has reported.
        self._reporting_nodes[side] |= 1 << index_node

        if self._reporting_nodes[side] == self._reference_value[side]:
            self._reporting_nodes[side] = 0
            return True
        else:
            return False

    def get_weight(self, node):
        """
        During backpropagation, each upstream node will need to
        know how important it is to our current node,
        represented by the weight of the incoming connection
        """
        return self._weights[node]

    @property
    def value(self):
        return self._value

    @property
    def node_type(self):
        return self.node_type

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, new_learning_rate: float):
        self._learning_rate = new_learning_rate


class FFNeurode(Neurode):
    # This class is inherited from Neurode.

    def __init__(self, my_type):
        super().__init__(my_type)

    @staticmethod
    def _sigmoid(value):
        # This should be a static method, and should
        # return the result of the sigmoid function at value.
        # 1 / (1 + e ^ -x)
        return 1 / (1 + np.exp(-value))

    def _calculate_value(self):
        """
        Calculate the weighted sum of the upstream nodes' values.
        Pass the result through self._sigmoid()
        store value into self._value
        """
        weighted_sum = 0
        for node, weight in self._weights.items():
            weighted_sum += node.value * weight
        self._value = self._sigmoid(weighted_sum)

    def _fire_downstream(self):
        """
        Call data_ready_upstream on each of this node's downstream neighbors,
        using self as an argument.
        """
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)

    def data_ready_upstream(self, node):
        """
        Call self._check_in() to register that the node has data.
        If self._check_in() indicates that all upstream nodes have data,
        it is time to collect that data and make it available to the next layer.
        Call self._calculate_value() and then self._fire_downstream().
        """
        if self._check_in(node, MultiLinkNode.Side.UPSTREAM):
            self._calculate_value()
            self._fire_downstream()

    def set_input(self, input_value):
        """
        This method is used by the client to directly set the value of an input layer neurode.
        The neurode does not need to do any processing, so it should simply set self._value,
        and then call data_ready_upstream() on all the downstream neighbors,
        passing self as an argument.
        """
        self._value = input_value
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)


class BPNeurode(Neurode):
    def __init__(self, my_type):
        super().__init__(my_type)
        self.delta = 0

    @staticmethod
    def _sigmoid_derivative(value):
        """
        This should be a static method, and calculates the derivative
        using the simplified formula f(x)* (1 - f(x)).
        Note:  the input/argument for this function should be f(x),
        the calculated value of the sigmoid function at x.
        """
        return value * (1 - value)

    """
    The expected parameter is only used for Output layer nodes.  Calculate the delta of this neurode as described in the lectures.  Note that there are different cases for hidden/input layer vs. output layer neurodes.  In either case, save the result to self._delta.  This method does not return any value.
    """
    def _calculate_delta(self, expected=None):
        if self._node_type == LayerType.OUTPUT:
            self.delta = self._sigmoid_derivative(self._value) * (expected - self._value)
        else:
            weighted_sum = 0
            for node, weight in self._weights.items():
                weighted_sum += node.delta * weight
            self.delta = self._sigmoid_derivative(self._value) * weighted_sum

    """
    def data_ready_downstream(self, node)
    Downstream neurodes call this method when they have data ready.  It should:

    Call self._check_in() to register that the node has data.
    If self._check_in() indicates that all downstream nodes have data, it is time to collect that data and make it available to the next layer up.  Call self._calculate_delta() and then self._fire_upstream().  Finally, call _update_weights().  The order is important here, and you should think carefully about how control is jumping around the network.  We want all the nodes to calculate delta before any of them updates weight...otherwise the new weights throw off the intended delta calculation.
    """
    def data_ready_downstream(self, node):
        if self._check_in(node, MultiLinkNode.Side.DOWNSTREAM):
            self._calculate_delta()
            self._fire_upstream()
            self._update_weights()

    """"
    def set_expected(self, expected_value)
    This method is used by the client to directly set the value of an output layer neurode.  The neurode should call self._calculate_delta to calculate and save its own delta...be sure to pass expected_value as an argument.  Call data_ready_downstream() on all of the upstream neighbors, passing self as an argument.
    """
    def set_expected(self, expected_value):
        self._calculate_delta(expected_value)
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    """
    def adjust_weights(self, node, adjustment)
    This method is called by an upstream node that is requesting to be more or less "important."  Use the node reference to add adjustment to the appropriate entry of self._weights.
    """
    def adjust_weights(self, node, adjustment):
        self._weights[node] += adjustment

    """
    def _update_weights(self)
    This method is the partner of adjust weights, and is called after delta is calculated.  This node will iterate through its downstream neighbors, and use adjust_weights to request an adjustment to the weight (importance) given to this node's data.  This is another (unusual) case where we will be passing self explicitly as an argument, to let the downstream node know who is calling.  Remember that the weight adjustment uses the downstream node's delta and learning rate, together with this node's value.
    """
    def _update_weights(self):
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.adjust_weights(self, self.delta * self._learning_rate * self._value)

    """
    def _fire_upstream(self)
    Call data_ready_downstream on each of this node's upstream neighbors, using self as an argument.  Note that this is safe for input nodes, as there are no downstream neighbors and the loop will never be entered.  Once more, this is an unusual example where we use "self" as an explicit argument.
    """
    def _fire_upstream(self):
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    """
    Property:
    Create a @property for self._delta.
    """
    @property
    def delta(self):
        return self._delta


"""
class FFBPNeurode()
After all that work, this will truly be easy.  This class will inherit from both FFNeurode and BPNeurode.  There is absolutely nothing more to do.
"""
class FFBPNeurode(FFNeurode, BPNeurode):
    pass
