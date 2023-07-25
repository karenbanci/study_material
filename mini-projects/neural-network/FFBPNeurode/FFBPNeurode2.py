from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import random
import math


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
        return 1 / (1 + math.exp(-value))

    def _calculate_value(self):
        """
        Calculate the weighted sum of the upstream nodes' values.
        Pass the result through self._sigmoid()
        store value into self._value
        """
        weighted_sum = 0
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            weighted_sum += node.value * self._weights[node]
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


def check_point_two_test():
    inodes = []
    hnodes = []
    onodes = []
    for k in range(2):
        inodes.append(FFNeurode(LayerType.INPUT))
    for k in range(2):
        hnodes.append(FFNeurode(LayerType.HIDDEN))
    onodes.append(FFNeurode(LayerType.OUTPUT))
    for node in inodes:
        node.reset_neighbors(hnodes, MultiLinkNode.Side.DOWNSTREAM)
    for node in hnodes:
        node.reset_neighbors(inodes, MultiLinkNode.Side.UPSTREAM)
        node.reset_neighbors(onodes, MultiLinkNode.Side.DOWNSTREAM)
    for node in onodes:
        node.reset_neighbors(hnodes, MultiLinkNode.Side.UPSTREAM)
    try:
        inodes[1].set_input(1)
        assert onodes[0].value == 0
    except:
        print("Error: Neurodes may be firing before receiving all input")
    inodes[0].set_input(0)

    # Since input node 0 has value of 0 and input node 1 has value of
    # one, the value of the hidden layers should be the sigmoid of the
    # weight out of input node 1.

    value_0 = (1 / (1 + np.exp(-hnodes[0]._weights[inodes[1]])))
    value_1 = (1 / (1 + np.exp(-hnodes[1]._weights[inodes[1]])))
    inter = onodes[0]._weights[hnodes[0]] * value_0 + \
            onodes[0]._weights[hnodes[1]] * value_1
    final = (1 / (1 + np.exp(-inter)))
    try:
        print(final, onodes[0].value)
        assert final == onodes[0].value
        assert 0 < final < 1
    except:
        print("Error: Calculation of neurode value may be incorrect")


check_point_two_test()

""" 
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/Project CS_3B_Winter_2023/CS_3B_Winter_2023/FFBPNeurode/FFBPNeurode2.py 
0.7628611090675722 0.7628611090675722

Process finished with exit code 0
"""
