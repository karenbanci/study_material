import copy
import random
from enum import Enum
from abc import ABC, abstractmethod


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
        :param reporting_nodes is a dictionary with two entries.
        The keys will be the two elements of the Side enum.  The values will initially be set to zero.
        We will use this as a binary encoding to keep track of which neighboring nodes have indicated
        that they have information available
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
        self._neighbors[side] = copy.copy(nodes)

        # Call _process_new_neighbor() for each node
        for node in nodes:
            self._process_new_neighbor(node, side)

        # Calculate and store the appropriate value in the correct element of self._reference_value.
        # represent what the reporting nodes value should be as a binary encoding when all the nodes have reported.
        self._reference_value[side] = (2 ** len(self._neighbors[side])) - 1

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
        # When an upstream neighbor is added, the node reference will be added as a key to the self._weights dictionary
        if side == MultiLinkNode.Side.UPSTREAM:
            #  The value related to this key should be a randomly generated float between 0 and 1
            self._weights[node] = random.uniform(0, 1)

    def _check_in(self, node, side):
        """
        This method will be called whenever the node learns that a neighboring node has information available.
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
        During backpropagation, each upstream node will need to know how important it is to our current node,
        represented by the weight of the incoming connection
        """
        return self._weights[node]

    # Create a property (getter only) for self._value (called value) and self._node_type (called node_type).
    # Create a property pair (getter and setter) for self._learning_rate (called learning_rate).
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
    def learning_rate(self, new_learning_rate):
        self._learning_rate = new_learning_rate


def check_point_one_test():
    # Mock up a network with three inputs and three outputs

    inputs = [Neurode(LayerType.INPUT) for _ in range(3)]
    outputs = [Neurode(LayerType.OUTPUT, .01) for _ in range(3)]
    if not inputs[0]._reference_value[MultiLinkNode.Side.DOWNSTREAM] == 0:
        print("Fail - Initial reference value is not zero")
    for node in inputs:
        node.reset_neighbors(outputs, MultiLinkNode.Side.DOWNSTREAM)
    for node in outputs:
        node.reset_neighbors(inputs, MultiLinkNode.Side.UPSTREAM)
    if not inputs[0]._reference_value[MultiLinkNode.Side.DOWNSTREAM] == 7:
        print("Fail - Final reference value is not correct")
    if not inputs[0]._reference_value[MultiLinkNode.Side.UPSTREAM] == 0:
        print("Fail - Final reference value is not correct")

    # Report data ready from each input and make sure _check_in
    # only reports True when all nodes have reported

    if not outputs[0]._reporting_nodes[MultiLinkNode.Side.UPSTREAM] == 0:
        print("Fail - Initial reporting value is not zero")
    if outputs[0]._check_in(inputs[0], MultiLinkNode.Side.UPSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in")
    if not outputs[0]._reporting_nodes[MultiLinkNode.Side.UPSTREAM] == 1:
        print("Fail - reporting value is not correct")
    if outputs[0]._check_in(inputs[2], MultiLinkNode.Side.UPSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in")
    if not outputs[0]._reporting_nodes[MultiLinkNode.Side.UPSTREAM] == 5:
        print("Fail - reporting value is not correct")
    if outputs[0]._check_in(inputs[2], MultiLinkNode.Side.UPSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in (double fire)")
    if not outputs[0]._reporting_nodes[MultiLinkNode.Side.UPSTREAM] == 5:
        print("Fail - reporting value is not correct")
    if not outputs[0]._check_in(inputs[1], MultiLinkNode.Side.UPSTREAM):
        print("Fail - _check_in returned False after all nodes were"
              "checked in")

    # Report data ready from each output and make sure _check_in
    # only reports True when all nodes have reported

    if inputs[1]._check_in(outputs[0], MultiLinkNode.Side.DOWNSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in")
    if inputs[1]._check_in(outputs[2], MultiLinkNode.Side.DOWNSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in")
    if inputs[1]._check_in(outputs[0], MultiLinkNode.Side.DOWNSTREAM):
        print("Fail - _check_in returned True but not all nodes were"
              "checked in (double fire)")
    if not inputs[1]._check_in(outputs[1], MultiLinkNode.Side.DOWNSTREAM):
        print("Fail - _check_in returned False after all nodes were"
              "checked in")

    # Check that learning rates were set correctly

    if not inputs[0].learning_rate == .05:
        print("Fail - default learning rate was not set")
    if not outputs[0].learning_rate == .01:
        print("Fail - specified learning rate was not set")

    # Check that weights appear random

    weight_list = list()
    for node in outputs:
        for t_node in inputs:
            if node.get_weight(t_node) in weight_list:
                print("Fail - weights do not appear to be set up properly")
            weight_list.append(node.get_weight(t_node))


check_point_one_test()


"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/Project CS_3B_Winter_2023/CS_3B_Winter_2023/FFBPNeurode/FFBPNeurode1.py 

Process finished with exit code 0
"""