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
    This is an abstract base class that will be the starting
    point for our eventual FFBPNeurode class.
    """

    class Side(Enum):
        """
        This is an Enum subclass of MultiLinkNode with elements
        UPSTREAM and DOWNSTREAM.
        We will use these terms to identify relationships between neurodes
        """
        UPSTREAM = 1
        DOWNSTREAM = 2

    def __init__(self):
        """
        The keys will be the two elements of the Side enum.
        The values will initially be set to zero.
        We will use this as a binary encoding to keep track of which
        neighboring nodes have indicated that they have information available
        """
        self._reporting_nodes = {MultiLinkNode.Side.UPSTREAM: 0,
                                 MultiLinkNode.Side.DOWNSTREAM: 0}
        self._reference_value = {MultiLinkNode.Side.UPSTREAM: 0,
                                 MultiLinkNode.Side.DOWNSTREAM: 0}
        self._neighbors = {MultiLinkNode.Side.UPSTREAM: [],
                           MultiLinkNode.Side.DOWNSTREAM: []}

    def __str__(self):
        """
        Overload this function to print out a representation
        of the node in context.
        """
        string = ""
        for upstream_neighbor in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            string += "\n upstream: " + str(id(upstream_neighbor))

        string += "\n self: " + str(id(self))

        for downstream_neighbor in \
                self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            string += "\n downstream: " + str(id(downstream_neighbor))

        return string

    @abstractmethod
    def _process_new_neighbor(self, node, side):
        """
        This is an abstract method that takes a node and
        a Side enum as parameters.
        """
        pass

    def reset_neighbors(self, nodes, side):
        # Copy the nodes parameter into the appropriate entry of
        # self._neighbors
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
        but we really are only concerned with upstream neighbors.
        """
        # When an upstream neighbor is added, the node reference
        # will be added as a key to the self._weights dictionary
        if side is MultiLinkNode.Side.UPSTREAM:
            #  The value related to this key should be a
            #  randomly generated float between 0 and 1
            self._weights[node] = random.random()

    def _check_in(self, node, side):
        """
        This method will be called whenever the node learns
        that a neighboring node has information available.
        :return True if every node has checked in reporting_nodes
        """
        # Find the node's index in self._neighbors.
        index_node = self._neighbors[side].index(node)

        """
        Use this index to update self._reporting_nodes to 
        reflect that this node has reported.
        """
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
        return self._node_type

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
        it is time to collect that data and make it available to the
        next layer. Call self._calculate_value() and then
        self._fire_downstream().
        """
        if self._check_in(node, MultiLinkNode.Side.UPSTREAM):
            self._calculate_value()
            self._fire_downstream()

    def set_input(self, input_value):
        """
        This method is used by the client to directly set the
        value of an input layer neurode.
        The neurode does not need to do any processing,
        so it should simply set self._value, and then
        call data_ready_upstream() on all the downstream neighbors,
        passing self as an argument.
        """
        self._value = input_value
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)


class BPNeurode(Neurode):
    def __init__(self, my_type):
        super().__init__(my_type)
        self._delta = 0

    @staticmethod
    def _sigmoid_derivative(value):
        """
        This should be a static method, and calculates the derivative
        using the simplified formula f(x)* (1 - f(x)).
        Note:  the input/argument for this function should be f(x),
        the calculated value of the sigmoid function at x.
        """
        return value * (1 - value)

    def _calculate_delta(self, expected_value=None):
        # The expected parameter is only used for Output layer nodes.
        # output nodes
        if self._node_type == LayerType.OUTPUT:
            #                   error                   *   sigmoid derivative
            self._delta = (expected_value - self._value) * \
                          self._sigmoid_derivative(self._value)

        # hidden nodes
        else:
            weighted_sum = 0
            for node_downstream in \
                    self.neighbors[MultiLinkNode.Side.DOWNSTREAM]:
                delta_downstream = node_downstream.delta
                weight_downstream = node_downstream.get_weight(self)
                weighted_sum += delta_downstream * weight_downstream

            #       (weighted sum of downstream delta) * (sigmoid derivative)
            self._delta = weighted_sum * self._sigmoid_derivative(self._value)

    def data_ready_downstream(self, node):
        # Call self._check_in() to register that the node has data.
        if self._check_in(node, MultiLinkNode.Side.DOWNSTREAM):
            self._calculate_delta()
            self._fire_upstream()
            self._update_weights()

    def set_expected(self, expected_value):
        """
        This method is used by the client to directly set
        the value of an output layer neurode.
        """
        self._calculate_delta(expected_value)
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    def adjust_weights(self, node, adjustment):
        """
        This method is called by an upstream node that is
        requesting to be more or less "important"
        Use the node reference to add adjustment to
        the appropriate entry of self._weights.
        """
        # adjustment is Vu*Dd*Lr
        self._weights[node] += adjustment

    def _update_weights(self):
        """
        This method is the partner of adjust weights,
        and is called after delta is calculated.
        This node will iterate through its downstream neighbors,
        and use adjust_weights to request an adjustment to the weight
        (importance) given to this node's data.
        """
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            adjustment = self._value * node.delta * self._learning_rate
            node.adjust_weights(self, adjustment)

    def _fire_upstream(self):
        """
        Call data_ready_downstream on each of this node's upstream neighbors,
        using self as an argument.
        """
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    @property
    def delta(self):
        return self._delta


class FFBPNeurode(FFNeurode, BPNeurode):
    """
     This class will inherit from both FFNeurode and BPNeurode.
     There is absolutely nothing more to do.
    """
    pass

class DoublyLinkedList:
    """
    Note that the DoublyLinkedList class is a generic data type separate
     from any conversation about neural networks.
     For this class DoublyLinkedList, any mention of "nodes" refers to
     a linked list node, not to a neurode.
    """
    class EmptyListError(BaseException):
        pass

    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def move_forward(self):
        """
        Move the current pointer forward one node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.next is None:
            raise IndexError
        self._curr = self._curr.next

    def move_back(self):
        """
        Move the current pointer back one node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.prev is None:
            raise IndexError
        self._curr = self._curr.prev

    def reset_to_head(self):
        """
        Reset the current pointer to the head of the list if the
        list is not empty.
        """
        if self._head is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._head

    def reset_to_tail(self):
        """
        Reset the current pointer to the tail of the list if the
        list is not empty.
        """
        if self._tail is None:
            raise DoublyLinkedList.EmptyListError
        self._curr = self._tail

    def add_to_head(self, data):
        """
        Add a new node to the head of the list.
        If the list is empty, the new node should also be the tail
        of the list. In either case, the current pointer should be reset
        to the head of the list.
        """
        new_node = DoublyLinkedList.Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._curr = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            self._curr = new_node

    def add_after_cur(self, data):
        """
        Add a new node after the current node.
        If the current node is the tail of the list,
        the new node should also be the tail of the list.
        In either case, the current pointer should not change
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError

        new_node = DoublyLinkedList.Node(data)

        if self._curr is self._tail:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        else:
            new_node.next = self._curr.next
            new_node.prev = self._curr
            self._curr.next.prev = new_node
            self._curr.next = new_node

    def remove_from_head(self):
        """
        Remove the node at the head of the list and return data.
        If the list is empty, raise an EmptyListError.
        If the list has only one node, the tail pointer should be set to None.
        In either case, the current pointer should be reset to the
        head of the list.
        """
        if self._head is None:
            raise DoublyLinkedList.EmptyListError
        if self._head is self._tail:
            data = self._head.data
            self._head = None
            self._tail = None
            self._curr = None
            return data
        else: # head is not tail
            data = self._head.data
            self._head = self._head.next
            self._head.prev = None
            self._curr = self._head
            return data

    def remove_after_cur(self):
        """
        If the list is empty, raise an EmptyListError.
        If the current node is the tail of the list, raise an IndexError.
        If the current node is the second to last node,
        the tail pointer should be set to the current node.
        In either case, the current pointer should not change.
        Remove the node after the current node and return data.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr is self._tail:
            raise IndexError
        if self._curr.next is self._tail:
            data = self._tail.data
            self._tail = self._curr
            self._tail.next = None
            return data
        else: # curr.next is not tail
            data = self._curr.next.data
            self._curr.next = self._curr.next.next
            self._curr.next.prev = self._curr
            return data

    def get_current_data(self):
        """
        If the list is empty, raise an EmptyListError.
        Return the data at the current node.
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        return self._curr.data


class LayerList(DoublyLinkedList):
    """
    Inputs represents the number of input layer neurodes.
    Outputs represents the number of output layer neurodes.
    Neurode_type is a dependency injection that gives us the flexibility
    to use a neurode class other than FFBPNeurode.
    Its type is Neurode, which guarantees that we have access to
    the methods that establish links between neurodes
    (reset_neighbors and _process_new_neighbor).
    """
    def __init__(self, inputs: int, outputs: int, neurode_type: Neurode):
        super().__init__()
        self._inputs = inputs
        self._input_list = []
        self._outputs = outputs
        self._outputs_list = []
        self._neurode_type = neurode_type
        """
        Inputs represents the number of input layer neurodes.
        Create that number of FFBPNeurode objects with LayerType 
        Input and place them in a list. 
        """
        for i in range(self._inputs):
            self._input_list.append(neurode_type(LayerType.INPUT))

        """
        outputs represents the number of output layer neurodes.
        Create that number of FFBPNeurode objects with LayerType 
        output and place them in a list. 
        """
        for i in range(self._outputs):
            self._outputs_list.append(neurode_type(LayerType.OUTPUT))

        # Use the Neurode methods to link these two layers together
        for n in self._input_list:
            n.reset_neighbors(self._outputs_list,
                              MultiLinkNode.Side.DOWNSTREAM)

        for n in self._outputs_list:
            n.reset_neighbors(self._input_list, MultiLinkNode.Side.UPSTREAM)

        # Add the input neurode list object to the doubly linked list
        self.add_to_head(self._input_list)
        # Add the output neurode list object to the doubly linked list
        self.add_after_cur(self._outputs_list)

    def add_layer(self, num_nodes: int):
        """"
        Will create a hidden layer of neurodes after the current layer
        (current linked list node).
        num_nodes specifies the number of LayerType
        Hidden neurodes in this hidden layer.
        Of course, raise an IndexError if the current layer is the
        output layer (tail of the linked list).
        """
        if self._curr == self._tail:
            raise IndexError
        else:
            # Create a hidden layer of neurodes after the current layer
            hidden_list = []
            for i in range(num_nodes):
                hidden_list.append(self._neurode_type(LayerType.HIDDEN))

            # Make sure the neurodes in this layer are correctly
            # linked with the upstream and downstream neurode neighbors.

            # link upstream list with hidden list
            upstream_list = self._curr.data
            for n in upstream_list:
                n.reset_neighbors(hidden_list,
                                  MultiLinkNode.Side.DOWNSTREAM)

            for n in hidden_list:
                n.reset_neighbors(upstream_list, MultiLinkNode.Side.UPSTREAM)

            # link downstream list with hidden list
            downstream_list = self._tail.data
            for n in hidden_list:
                n.reset_neighbors(downstream_list,
                                  MultiLinkNode.Side.DOWNSTREAM)

            for n in downstream_list:
                n.reset_neighbors(hidden_list, MultiLinkNode.Side.UPSTREAM)

            self.add_after_cur(hidden_list)
            # self.move_forward()

    def remove_layer(self):
        """
        Will remove the current layer (current linked list node)
        and all neurodes in that layer.
        Of course, raise an EmptyListError if the list is empty,
        and raise an IndexError if the current layer is the input layer
        (head of the linked list).
        """
        if self._curr is None:
            raise DoublyLinkedList.EmptyListError
        if self._curr.next == self._tail:
            raise IndexError
        else:
            self.remove_after_cur()
        # Be sure that the neurodes in the remaining layers are
        # correctly linked
        current_list = self.get_current_data()
        downstream_list = self._curr.next.data
        for n in current_list:
            n.reset_neighbors(downstream_list, MultiLinkNode.Side.DOWNSTREAM)

        for n in downstream_list:
            n.reset_neighbors(current_list, MultiLinkNode.Side.UPSTREAM)

    @property
    def input_nodes(self):
        """
        Return a list of the neurodes in the input layer.
        """
        return self._input_list

    @property
    def output_nodes(self):
        """
        Return a list of the neurodes in the output layer.
        """
        return self._outputs_list


def layer_list_test():
    # create a LayerList with two inputs and four outputs
    my_list = LayerList(2, 4, FFBPNeurode)
    # get a list of the input and output nodes, and make sure we have
    # the right number
    inputs = my_list.input_nodes
    outputs = my_list.output_nodes
    assert len(inputs) == 2
    assert len(outputs) == 4
    # check that each has the right number of connections
    for node in inputs:
        assert len(node._neighbors[FFBPNeurode.Side.DOWNSTREAM]) == 4
    for node in outputs:
        assert len(node._neighbors[FFBPNeurode.Side.UPSTREAM]) == 2
    # check that the connections go to the right place
    for node in inputs:
        out_set = set(node._neighbors[FFBPNeurode.Side.DOWNSTREAM])
        check_set = set(outputs)
        assert out_set == check_set
    for node in outputs:
        in_set = set(node._neighbors[FFBPNeurode.Side.UPSTREAM])
        check_set = set(inputs)
        assert in_set == check_set
    # add a couple layers and check that they arrived in the right order, and that iterate and rev_iterate work
    my_list.reset_to_head()
    my_list.add_layer(3)
    my_list.add_layer(6)
    my_list.move_forward()
    assert my_list.get_current_data()[0].node_type == LayerType.HIDDEN
    assert len(my_list.get_current_data()) == 6
    my_list.move_forward()
    assert my_list.get_current_data()[0].node_type == LayerType.HIDDEN
    assert len(my_list.get_current_data()) == 3
    # save this layer to make sure it gets properly removed later
    my_list.move_forward()
    assert my_list.get_current_data()[0].node_type == LayerType.OUTPUT
    assert len(my_list.get_current_data()) == 4
    my_list.move_back()
    assert my_list.get_current_data()[0].node_type == LayerType.HIDDEN
    assert len(my_list.get_current_data()) == 3
    # check that information flows through all layers
    save_vals = []
    for node in outputs:
        save_vals.append(node.value)
    for node in inputs:
        node.set_input(1)
    for i, node in enumerate(outputs):
        assert save_vals[i] != node.value
    # check that information flows back as well
    save_vals = []
    for node in inputs[1]._neighbors[FFBPNeurode.Side.DOWNSTREAM]:
        save_vals.append(node.delta)
    for node in outputs:
        node.set_expected(1)
    for i, node in enumerate(inputs[1]._neighbors[FFBPNeurode.Side.DOWNSTREAM]):
        assert save_vals[i] != node.delta
    # try to remove an output layer
    try:
        my_list.remove_layer()
        assert False
    except IndexError:
        pass
    except:
        assert False
    # move and remove a hidden layer
    save_list = my_list.get_current_data()
    my_list.move_back()
    my_list.remove_layer()
    # check the order of layers again
    my_list.reset_to_head()
    assert my_list.get_current_data()[0].node_type == LayerType.INPUT
    assert len(my_list.get_current_data()) == 2
    my_list.move_forward()
    assert my_list.get_current_data()[0].node_type == LayerType.HIDDEN
    assert len(my_list.get_current_data()) == 6
    my_list.move_forward()
    assert my_list.get_current_data()[0].node_type == LayerType.OUTPUT
    assert len(my_list.get_current_data()) == 4
    my_list.move_back()
    assert my_list.get_current_data()[0].node_type == LayerType.HIDDEN
    assert len(my_list.get_current_data()) == 6
    my_list.move_back()
    assert my_list.get_current_data()[0].node_type == LayerType.INPUT
    assert len(my_list.get_current_data()) == 2
    # save a value from the removed layer to make sure it doesn't get changed
    saved_val = save_list[0].value
    # check that information still flows through all layers
    save_vals = []
    for node in outputs:
        save_vals.append(node.value)
    for node in inputs:
        node.set_input(1)
    for i, node in enumerate(outputs):
        assert save_vals[i] != node.value
    # check that information still flows back as well
    save_vals = []
    for node in inputs[1]._neighbors[FFBPNeurode.Side.DOWNSTREAM]:
        save_vals.append(node.delta)
    for node in outputs:
        node.set_expected(1)
    for i, node in enumerate(inputs[1]._neighbors[FFBPNeurode.Side.DOWNSTREAM]):
        assert save_vals[i] != node.delta
    assert saved_val == save_list[0].value


layer_list_test()

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/
Project CS_3B_Winter_2023/CS_3B_Winter_2023/LayerList/LayerList2.py 

Process finished with exit code 0
"""