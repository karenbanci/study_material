from abc import ABC, abstractmethod
import collections
from enum import Enum
import numpy as np
import random
import math


class DataMismatchError(Exception):
    """
    NNData will enforce there must be exactly as many labels as features, and
    raise a DataMismatchError
    exception if the set sizes do not match.
    """
    pass


class NNData:
    """
    NNData will store data and deliver it in a way that is meaningful to the
    neural network.
    """

    class Set(Enum):
        TRAIN = 1
        TEST = 2

    class Order(Enum):
        RANDOM = 1
        SEQUENTIAL = 2

    def __init__(self, features=None, labels=None, train_factor=0.9):
        """
        Will accept two lists-of-lists, one features and another one labels,
        and train_factor which defines
        how much of the data will be allocated to the training set.

        :param features: Be part of lists-of-list. Each row representing the
        features of one example from our data.
        :param labels: Be part of lists-of-lists. Each row representing one
        label from our data.
        :param train_factor: Represents the percentage of the data we want
        used as our training set.
        :param train_indices: To point to the items in our dataset that make
        up the training set.
        :param test_indices: To point to the items in our dataset that make
        up the testing set.
        :param train_pool: To keep track of which training items have not
        yet been seen in a particular training epoch.
        :param test_pool: To keep track of which training items have not
        yet been seen in a testing run.
        """
        self._features = None
        self._labels = None
        self._train_factor = NNData.percentage_limiter(train_factor)
        self._train_indices = []
        self._test_indices = []
        self._train_pool = collections.deque()
        self._test_pool = collections.deque()

        if features is None:
            features = []
        if labels is None:
            labels = []

        self.load_data(features, labels)

    @staticmethod
    def percentage_limiter(percentage):
        """
        Accepts percentage as a float and returns 0 if percentage < 0,
        1 if percentage is > 1, or percentage if 0 <= percentage <= 1.
        """
        if percentage < 0:
            return 0
        elif percentage > 1:
            return 1
        else:
            return percentage

    def empty_data(self):
        """
        This method avoids repeated code that will be used to empty data
        in load_data()
        """
        self._features = None
        self._labels = None

    def empty_data_and_split_set(self):
        """
        This method avoids repeated code that will be used to empty data
        in load_data()
        """
        self.empty_data()
        self.split_set()

    def load_data(self, features, labels):
        """
        Method that can be used to load or re-load data. This method was
        used by the constructor,but can also be called directly by the client.
        Besides that, creates numpy arrays from features and labels
        and assign them to self._features and self._labels. Validation
        to ensure that the provided data is
        consistent and of type float.
        :param features: Will be used when creating an array of self._features
        :param labels: Will be used when creating an array of self._labels
        """
        if features is None or labels is None:
            self.empty_data()
            return

        if len(features) != len(labels):
            self.empty_data_and_split_set()
            raise DataMismatchError
        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self.empty_data_and_split_set()
            raise ValueError
        # To ensure that the indices line up with newly loaded data
        self.split_set()

    def prime_data(self, target_set=None, order=None):
        """
        This method will load one or both deques to be used as indirect indices
        :param target_set: Will dictate whether we are loading self._train_pool
        :param order: If order is NNData.Order.RANDOM, shuffle the pool(s)
        If order is None or NNData.Order.SEQUENTIAL, leave the pool(s) in order
        """
        # Loading self._train_pool (if target_set is NNData.Set.TRAIN)
        if target_set == NNData.Set.TRAIN:
            self._train_pool = collections.deque(self._train_indices)
        # Loading self._test_pool (if target_set is NNData.Set.TEST)
        elif target_set == NNData.Set.TEST:
            self._test_pool = collections.deque(self._test_indices)
        # Load both pools.
        else:
            self._train_pool = collections.deque(self._train_indices)
            self._test_pool = collections.deque(self._test_indices)

        if order == NNData.Order.RANDOM:
            # shuffle pools
            random.shuffle(self._train_pool)
            random.shuffle(self._test_pool)
        elif order is None or order == NNData.Order.SEQUENTIAL:
            pass

    def get_one_item(self, target_set=None):
        """
        This method will deliver feature and label data for one example from
        either the training set or the testing set (client specifies which set
        is desired).
        """
        if target_set == NNData.Set.TRAIN or target_set is None:
            try:
                current_index = self._train_pool.popleft()
            except IndexError:
                return None

        else:  # Assuming target_set == NNData.Set.TEST:
            try:
                current_index = self._test_pool.popleft()
            except IndexError:
                return None

        current_feature = self._features[current_index]
        current_label = self._labels[current_index]
        current_tuple = (current_feature, current_label)
        return current_tuple

    def split_set(self, new_train_factor=None):
        """
        Shuffle all the examples and randomly assign them to the testing or
        training set, based on the training factor
        :param new_train_factor: It is the new value to train_factor.
        """
        if new_train_factor is not None:
            self._train_factor = NNData.percentage_limiter(new_train_factor)

        # Just do validation
        if self._features is None or self._labels is None:
            return

        number_of_examples = len(self._features)
        # Calculate and store the number of examples that should be used for
        # training
        number_of_examples_for_training = number_of_examples * \
                                          self._train_factor
        random_list = list(range(number_of_examples))
        random.shuffle(random_list)
        try:
            self._train_indices = random_list[
                                  :int(number_of_examples_for_training)]
            self._test_indices = random_list[
                                 int(number_of_examples_for_training):]
        except Exception as e:
            print(e)
        self.prime_data()

    def number_of_samples(self, target_set=None):
        """
        This method will return the number of examples in the testing set,
        the training set, or both combined (client specifies which set
        is desired).
        """
        if target_set == NNData.Set.TEST:
            # total number of testing examples
            return len(self._test_indices)
        elif target_set == NNData.Set.TRAIN:
            # total number of training examples
            return len(self._train_indices)
        else:
            # both combined
            return len(self._test_indices) + len(self._train_indices)

    def pool_is_empty(self, target_set=None):
        """
        This method will return True when either the training set or
        testing set is exhausted (client specifies which set is desired).
        : param target_set: Is an Enum of type NNData.Set, or None.
        """
        if target_set == NNData.Set.TRAIN or target_set is None:
            if len(self._train_pool) == 0:
                return True
            else:
                return False
        elif target_set == NNData.Set.TEST:
            if len(self._test_pool) == 0:
                return True
            else:
                return False


def load_XOR():
    """
    Spawns a new NNData object using these features and  labels. Sets a
    train factor of 1.
    """
    NNData(features=[[0, 0], [1, 0], [0, 1], [1, 1]],
           labels=[[0], [1], [1], [0]],
           train_factor=1)


load_XOR()


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
        else:  # head is not tail
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
        else:  # curr.next is not tail
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


class EmptySetException(Exception):
    pass


class FFBPNetwork:
    """
    This class will use LayerList to create a network, and will provide
    training and testing methods that take advantage of the NNData
    """

    def __init__(self, num_inputs: int, num_outputs: int):
        """
        num_inputs is the number of input neurodes in the input layer.
        num_outputs is the number of output neurodes in the output layer.
        """
        self._num_inputs = num_inputs
        self._num_outputs = num_outputs
        self._layer_list = LayerList(num_inputs, num_outputs, FFBPNeurode)

    def add_hidden_layer(self, num_nodes: int, position = 0):
        """
        Will add a hidden layer of num_nodes neurodes after the
        position-th hidden layer.
        """
        if position > 0:
            for i in range(position):
                self._layer_list.move_forward()

        self._layer_list.add_layer(num_nodes)

    def train(self, data_set: NNData, epochs=1000,
              verbosity=2, order=NNData.Order.RANDOM):
        """"
        Will train the network using the data in data_set.
        :param data_set is an NNData object.
        :param epochs is the number of times to iterate through the data_set.
        :param verbosity is the level of detail to print during training.
        :param order is the order in which to present the data to the network.
        """
        if data_set.number_of_samples(NNData.Set.TRAIN) == 0:
            raise EmptySetException
        else:
            rmse = 0
            for epoch in range(epochs):
                data_set.prime_data(NNData.Set.TRAIN, order)
                # while training set is not exhausted:
                epoch_error = 0
                while not data_set.pool_is_empty():
                    features, labels = data_set.get_one_item(NNData.Set.TRAIN)
                    # present the feature list to the input neurodes
                    sample_error = 0
                    for index, input_neurode in \
                            enumerate(self._layer_list.input_nodes):
                        input_neurode.set_input(features[index])
                    # check the values at the output neurodes and calculate
                    # the error
                    for index, output_neurode in \
                            enumerate(self._layer_list.output_nodes):
                        output_value = output_neurode.value
                        error_value = labels[index] - output_value
                        sample_error += error_value ** 2
                        if verbosity > 2:
                            print(f"output_value: {output_value}")
                            print(f"label: {labels[index]}")
                            print(f"error_value: {error_value}")
                        output_neurode.set_expected(labels[index])
                    epoch_error += math.sqrt(sample_error/labels.shape[0])

                    if verbosity > 1 and epoch % 1000 == 0:
                        print(f"Feature: {features}, Label: {labels}")
                        for index, output_node in \
                                enumerate(self._layer_list.output_nodes):
                            print("Output: ",
                              self._layer_list.output_nodes[index].value)

                if verbosity > 0 and epoch % 100 == 0:
                    rmse = epoch_error / \
                           data_set.number_of_samples(NNData.Set.TRAIN)
                    print(f"Epoch: {epoch} RMSE = {rmse}")
        print(f"Training finished.\n Final Training RMSE = {rmse} ")

    def test(self, data_set: NNData, order=NNData.Order.SEQUENTIAL):
        """
        This public method will test the network.
        It will use the testing set rather than the training set
        If will only go through the dataset once
        It will report the input, expected and output value for each example
        It will report RMSE at the end of the test
        """
        print("\n----- starting test")
        if data_set.number_of_samples(NNData.Set.TEST) == 0:
            raise EmptySetException
        else:
            # prepare data, once
            data_set.prime_data(NNData.Set.TEST, order)
            total_error = 0
            # while training set is not exhausted:
            while not data_set.pool_is_empty(target_set=NNData.Set.TEST):
                features, labels = data_set.get_one_item(NNData.Set.TEST)
                # present the feature list to the input neurodes
                sample_error = 0

                for index, input_neurode in \
                        enumerate(self._layer_list.input_nodes):
                    input_neurode.set_input(features[index])
                    print(f"input_value: {features[index]}")

                for index, output_neurode in \
                        enumerate(self._layer_list.output_nodes):
                    output_value = output_neurode.value
                    error_value = labels[index] - output_value
                    sample_error += error_value ** 2
                    print(f"output_value: {output_value}")
                    print(f"expected_value: {labels[index]}")
                    # print("error_value", error_value)
                total_error += math.sqrt(sample_error / labels.shape[0])
            rmse = total_error / data_set.number_of_samples(NNData.Set.TEST)
            # print(f"Feature: {features} , Label: {labels}")
            print(f"Final Testing RMSE = {rmse}")


def run_iris():
    network = FFBPNetwork(4, 3)
    network.add_hidden_layer(3)
    Iris_X = [[5.1, 3.5, 1.4, 0.2], [4.9, 3, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [4.6, 3.1, 1.5, 0.2],
              [5, 3.6, 1.4, 0.2], [5.4, 3.9, 1.7, 0.4], [4.6, 3.4, 1.4, 0.3], [5, 3.4, 1.5, 0.2],
              [4.4, 2.9, 1.4, 0.2], [4.9, 3.1, 1.5, 0.1], [5.4, 3.7, 1.5, 0.2], [4.8, 3.4, 1.6, 0.2],
              [4.8, 3, 1.4, 0.1], [4.3, 3, 1.1, 0.1], [5.8, 4, 1.2, 0.2], [5.7, 4.4, 1.5, 0.4],
              [5.4, 3.9, 1.3, 0.4], [5.1, 3.5, 1.4, 0.3], [5.7, 3.8, 1.7, 0.3], [5.1, 3.8, 1.5, 0.3],
              [5.4, 3.4, 1.7, 0.2], [5.1, 3.7, 1.5, 0.4], [4.6, 3.6, 1, 0.2], [5.1, 3.3, 1.7, 0.5],
              [4.8, 3.4, 1.9, 0.2], [5, 3, 1.6, 0.2], [5, 3.4, 1.6, 0.4], [5.2, 3.5, 1.5, 0.2],
              [5.2, 3.4, 1.4, 0.2], [4.7, 3.2, 1.6, 0.2], [4.8, 3.1, 1.6, 0.2], [5.4, 3.4, 1.5, 0.4],
              [5.2, 4.1, 1.5, 0.1], [5.5, 4.2, 1.4, 0.2], [4.9, 3.1, 1.5, 0.1], [5, 3.2, 1.2, 0.2],
              [5.5, 3.5, 1.3, 0.2], [4.9, 3.1, 1.5, 0.1], [4.4, 3, 1.3, 0.2], [5.1, 3.4, 1.5, 0.2],
              [5, 3.5, 1.3, 0.3], [4.5, 2.3, 1.3, 0.3], [4.4, 3.2, 1.3, 0.2], [5, 3.5, 1.6, 0.6],
              [5.1, 3.8, 1.9, 0.4], [4.8, 3, 1.4, 0.3], [5.1, 3.8, 1.6, 0.2], [4.6, 3.2, 1.4, 0.2],
              [5.3, 3.7, 1.5, 0.2], [5, 3.3, 1.4, 0.2], [7, 3.2, 4.7, 1.4], [6.4, 3.2, 4.5, 1.5],
              [6.9, 3.1, 4.9, 1.5], [5.5, 2.3, 4, 1.3], [6.5, 2.8, 4.6, 1.5], [5.7, 2.8, 4.5, 1.3],
              [6.3, 3.3, 4.7, 1.6], [4.9, 2.4, 3.3, 1], [6.6, 2.9, 4.6, 1.3], [5.2, 2.7, 3.9, 1.4], [5, 2, 3.5, 1],
              [5.9, 3, 4.2, 1.5], [6, 2.2, 4, 1], [6.1, 2.9, 4.7, 1.4], [5.6, 2.9, 3.6, 1.3], [6.7, 3.1, 4.4, 1.4],
              [5.6, 3, 4.5, 1.5], [5.8, 2.7, 4.1, 1], [6.2, 2.2, 4.5, 1.5], [5.6, 2.5, 3.9, 1.1],
              [5.9, 3.2, 4.8, 1.8], [6.1, 2.8, 4, 1.3], [6.3, 2.5, 4.9, 1.5], [6.1, 2.8, 4.7, 1.2],
              [6.4, 2.9, 4.3, 1.3], [6.6, 3, 4.4, 1.4], [6.8, 2.8, 4.8, 1.4], [6.7, 3, 5, 1.7], [6, 2.9, 4.5, 1.5],
              [5.7, 2.6, 3.5, 1], [5.5, 2.4, 3.8, 1.1], [5.5, 2.4, 3.7, 1], [5.8, 2.7, 3.9, 1.2],
              [6, 2.7, 5.1, 1.6], [5.4, 3, 4.5, 1.5], [6, 3.4, 4.5, 1.6], [6.7, 3.1, 4.7, 1.5],
              [6.3, 2.3, 4.4, 1.3], [5.6, 3, 4.1, 1.3], [5.5, 2.5, 4, 1.3], [5.5, 2.6, 4.4, 1.2],
              [6.1, 3, 4.6, 1.4], [5.8, 2.6, 4, 1.2], [5, 2.3, 3.3, 1], [5.6, 2.7, 4.2, 1.3], [5.7, 3, 4.2, 1.2],
              [5.7, 2.9, 4.2, 1.3], [6.2, 2.9, 4.3, 1.3], [5.1, 2.5, 3, 1.1], [5.7, 2.8, 4.1, 1.3],
              [6.3, 3.3, 6, 2.5], [5.8, 2.7, 5.1, 1.9], [7.1, 3, 5.9, 2.1], [6.3, 2.9, 5.6, 1.8],
              [6.5, 3, 5.8, 2.2], [7.6, 3, 6.6, 2.1], [4.9, 2.5, 4.5, 1.7], [7.3, 2.9, 6.3, 1.8],
              [6.7, 2.5, 5.8, 1.8], [7.2, 3.6, 6.1, 2.5], [6.5, 3.2, 5.1, 2], [6.4, 2.7, 5.3, 1.9],
              [6.8, 3, 5.5, 2.1], [5.7, 2.5, 5, 2], [5.8, 2.8, 5.1, 2.4], [6.4, 3.2, 5.3, 2.3], [6.5, 3, 5.5, 1.8],
              [7.7, 3.8, 6.7, 2.2], [7.7, 2.6, 6.9, 2.3], [6, 2.2, 5, 1.5], [6.9, 3.2, 5.7, 2.3],
              [5.6, 2.8, 4.9, 2], [7.7, 2.8, 6.7, 2], [6.3, 2.7, 4.9, 1.8], [6.7, 3.3, 5.7, 2.1],
              [7.2, 3.2, 6, 1.8], [6.2, 2.8, 4.8, 1.8], [6.1, 3, 4.9, 1.8], [6.4, 2.8, 5.6, 2.1],
              [7.2, 3, 5.8, 1.6], [7.4, 2.8, 6.1, 1.9], [7.9, 3.8, 6.4, 2], [6.4, 2.8, 5.6, 2.2],
              [6.3, 2.8, 5.1, 1.5], [6.1, 2.6, 5.6, 1.4], [7.7, 3, 6.1, 2.3], [6.3, 3.4, 5.6, 2.4],
              [6.4, 3.1, 5.5, 1.8], [6, 3, 4.8, 1.8], [6.9, 3.1, 5.4, 2.1], [6.7, 3.1, 5.6, 2.4],
              [6.9, 3.1, 5.1, 2.3], [5.8, 2.7, 5.1, 1.9], [6.8, 3.2, 5.9, 2.3], [6.7, 3.3, 5.7, 2.5],
              [6.7, 3, 5.2, 2.3], [6.3, 2.5, 5, 1.9], [6.5, 3, 5.2, 2], [6.2, 3.4, 5.4, 2.3], [5.9, 3, 5.1, 1.8]]
    Iris_Y = [[1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ], [1, 0, 0, ],
              [1, 0, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ], [0, 1, 0, ],
              [0, 1, 0, ], [0, 1, 0, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ],
              [0, 0, 1, ], [0, 0, 1, ], [0, 0, 1, ]]
    data = NNData(Iris_X, Iris_Y, .7)
    network.train(data, 10001, order=NNData.Order.RANDOM)
    network.test(data)


def run_sin():
    network = FFBPNetwork(1, 1)
    network.add_hidden_layer(3)
    sin_X = [[0], [0.01], [0.02], [0.03], [0.04], [0.05], [0.06], [0.07], [0.08], [0.09], [0.1], [0.11], [0.12],
             [0.13], [0.14], [0.15], [0.16], [0.17], [0.18], [0.19], [0.2], [0.21], [0.22], [0.23], [0.24], [0.25],
             [0.26], [0.27], [0.28], [0.29], [0.3], [0.31], [0.32], [0.33], [0.34], [0.35], [0.36], [0.37], [0.38],
             [0.39], [0.4], [0.41], [0.42], [0.43], [0.44], [0.45], [0.46], [0.47], [0.48], [0.49], [0.5], [0.51],
             [0.52], [0.53], [0.54], [0.55], [0.56], [0.57], [0.58], [0.59], [0.6], [0.61], [0.62], [0.63], [0.64],
             [0.65], [0.66], [0.67], [0.68], [0.69], [0.7], [0.71], [0.72], [0.73], [0.74], [0.75], [0.76], [0.77],
             [0.78], [0.79], [0.8], [0.81], [0.82], [0.83], [0.84], [0.85], [0.86], [0.87], [0.88], [0.89], [0.9],
             [0.91], [0.92], [0.93], [0.94], [0.95], [0.96], [0.97], [0.98], [0.99], [1], [1.01], [1.02], [1.03],
             [1.04], [1.05], [1.06], [1.07], [1.08], [1.09], [1.1], [1.11], [1.12], [1.13], [1.14], [1.15], [1.16],
             [1.17], [1.18], [1.19], [1.2], [1.21], [1.22], [1.23], [1.24], [1.25], [1.26], [1.27], [1.28], [1.29],
             [1.3], [1.31], [1.32], [1.33], [1.34], [1.35], [1.36], [1.37], [1.38], [1.39], [1.4], [1.41], [1.42],
             [1.43], [1.44], [1.45], [1.46], [1.47], [1.48], [1.49], [1.5], [1.51], [1.52], [1.53], [1.54], [1.55],
             [1.56], [1.57]]
    sin_Y = [[0], [0.00999983333416666], [0.0199986666933331], [0.0299955002024957], [0.0399893341866342],
             [0.0499791692706783], [0.0599640064794446], [0.0699428473375328], [0.0799146939691727],
             [0.089878549198011], [0.0998334166468282], [0.109778300837175], [0.119712207288919],
             [0.129634142619695], [0.139543114644236], [0.149438132473599], [0.159318206614246],
             [0.169182349066996], [0.179029573425824], [0.188858894976501], [0.198669330795061], [0.2084598998461],
             [0.218229623080869], [0.227977523535188], [0.237702626427135], [0.247403959254523],
             [0.257080551892155], [0.266731436688831], [0.276355648564114], [0.285952225104836], [0.29552020666134],
             [0.305058636443443], [0.314566560616118], [0.324043028394868], [0.333487092140814],
             [0.342897807455451], [0.35227423327509], [0.361615431964962], [0.370920469412983], [0.380188415123161],
             [0.389418342308651], [0.398609327984423], [0.40776045305957], [0.416870802429211], [0.425939465066],
             [0.43496553411123], [0.44394810696552], [0.452886285379068], [0.461779175541483], [0.470625888171158],
             [0.479425538604203], [0.488177246882907], [0.496880137843737], [0.505533341204847],
             [0.514135991653113], [0.522687228930659], [0.531186197920883], [0.539632048733969],
             [0.548023936791874], [0.556361022912784], [0.564642473395035], [0.572867460100481],
             [0.581035160537305], [0.58914475794227], [0.597195441362392], [0.60518640573604], [0.613116851973434],
             [0.62098598703656], [0.628793024018469], [0.636537182221968], [0.644217687237691], [0.651833771021537],
             [0.659384671971473], [0.666869635003698], [0.674287911628145], [0.681638760023334],
             [0.688921445110551], [0.696135238627357], [0.70327941920041], [0.710353272417608], [0.717356090899523],
             [0.724287174370143], [0.731145829726896], [0.737931371109963], [0.744643119970859],
             [0.751280405140293], [0.757842562895277], [0.764328937025505], [0.770738878898969],
             [0.777071747526824], [0.783326909627483], [0.78950373968995], [0.795601620036366], [0.801619940883777],
             [0.807558100405114], [0.813415504789374], [0.819191568300998], [0.82488571333845], [0.83049737049197],
             [0.836025978600521], [0.841470984807897], [0.846831844618015], [0.852108021949363],
             [0.857298989188603], [0.862404227243338], [0.867423225594017], [0.872355482344986],
             [0.877200504274682], [0.881957806884948], [0.886626914449487], [0.891207360061435],
             [0.895698685680048], [0.900100442176505], [0.904412189378826], [0.908633496115883],
             [0.912763940260521], [0.916803108771767], [0.920750597736136], [0.92460601240802], [0.928368967249167],
             [0.932039085967226], [0.935616001553386], [0.939099356319068], [0.942488801931697],
             [0.945783999449539], [0.948984619355586], [0.952090341590516], [0.955100855584692],
             [0.958015860289225], [0.960835064206073], [0.963558185417193], [0.966184951612734],
             [0.968715100118265], [0.971148377921045], [0.973484541695319], [0.975723357826659],
             [0.977864602435316], [0.979908061398614], [0.98185353037236], [0.983700814811277], [0.98544972998846],
             [0.98710010101385], [0.98865176285172], [0.990104560337178], [0.991458348191686], [0.992712991037588],
             [0.993868363411645], [0.994924349777581], [0.99588084453764], [0.996737752043143], [0.997494986604054],
             [0.998152472497548], [0.998710143975583], [0.999167945271476], [0.999525830605479],
             [0.999783764189357], [0.999941720229966], [0.999999682931835]]
    data = NNData(sin_X, sin_Y, .1)
    network.train(data, 10001, order=NNData.Order.RANDOM)
    network.test(data)


def run_XOR():
    network = FFBPNetwork(2, 1)
    network.add_hidden_layer(5)
    data = NNData(features=[
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1]],
           labels=[
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0]],
           train_factor=.8)
    network.train(data, 10001, order=NNData.Order.RANDOM)
    network.test(data)


if __name__ == "__main__":
    print("\n----------------------------------------------------- Run Iris")
    run_iris()

    print("\n\n--------------------------------------------------- Run Sin")
    run_sin()

    print("\n\n--------------------------------------------------- Run XOR")
    run_XOR()

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/
Project CS_3B_Winter_2023/CS_3B_Winter_2023/Assingment5/
CompleteNeuralNetworkFinal.py 

----------------------------------------------------- Run Iris
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.9983509466973912
Output:  0.9999758678475459
Output:  0.9999119936795103
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  0.9994970997457635
Output:  0.9999978160728742
Output:  0.9999808296829967
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9966337011099113
Output:  0.999896784437902
Output:  0.9998611887275859
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9965032706490782
Output:  0.9999002407619859
Output:  0.9998624155570035
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.9986444103875316
Output:  0.9999807224633849
Output:  0.9999257548111711
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.9953106865015967
Output:  0.9998432991650236
Output:  0.9996516864585921
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9935029140354658
Output:  0.9997749139495195
Output:  0.9997199009149736
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  0.9987592385540535
Output:  0.9999843464010182
Output:  0.9999301829354743
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.9984675410423177
Output:  0.9999626874724424
Output:  0.9998702319142785
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  0.9994203546357766
Output:  0.999994280492303
Output:  0.9999612491436664
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.9977661227689184
Output:  0.9999461393993493
Output:  0.9998322680824202
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  0.9990555837395041
Output:  0.9999911577797144
Output:  0.9999434695393169
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  0.999133045780358
Output:  0.9999954437366347
Output:  0.9999691887523389
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9934960606403371
Output:  0.9997749048284963
Output:  0.9997198748835373
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  0.9994502536563742
Output:  0.9999981817242228
Output:  0.9999835763881927
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9926686661669921
Output:  0.999766262833084
Output:  0.999701244292247
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9962650570465066
Output:  0.9999072821403732
Output:  0.9998722662659161
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.9976982218347066
Output:  0.9999559791619465
Output:  0.999871589943838
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  0.9994121130552098
Output:  0.9999963622398834
Output:  0.9999740531773645
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9952654128558838
Output:  0.9998772139112041
Output:  0.9998117951654844
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9974702727018923
Output:  0.9999458565730394
Output:  0.9999240554578225
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  0.9989099428269048
Output:  0.9999903209061116
Output:  0.9999423394594329
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.994358835648621
Output:  0.9997765588142247
Output:  0.999743593453536
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.9966898633226737
Output:  0.9999410858035876
Output:  0.9998447176045447
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  0.9995490633269153
Output:  0.9999979777266719
Output:  0.9999821433088594
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.998722965690159
Output:  0.9999896897885209
Output:  0.9999570015890994
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9971075427021996
Output:  0.9999130764018097
Output:  0.9998689564414353
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.9983230499548313
Output:  0.9999789959784768
Output:  0.9999240223452234
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  0.9978044898905974
Output:  0.9999670040152454
Output:  0.9998623637108404
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.9984501813905361
Output:  0.9999757403645132
Output:  0.9999121859435747
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.9949555780756177
Output:  0.9998475814815668
Output:  0.9996548111472003
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.9989558352322643
Output:  0.9999916249149291
Output:  0.9999572590967638
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9934765558879489
Output:  0.9997748662124726
Output:  0.9997197717304583
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.9988382685333531
Output:  0.9999879904302851
Output:  0.9999499874028691
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9980273986056417
Output:  0.9999662523490483
Output:  0.999946509441711
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.995281584910113
Output:  0.99990860129225
Output:  0.9998724587228827
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  0.9985990758773213
Output:  0.9999777057903998
Output:  0.9998939566675296
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  0.9993464376113279
Output:  0.9999961892380227
Output:  0.9999722229349151
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  0.9987443980435048
Output:  0.999984095843956
Output:  0.9999082885468825
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.9982305327616849
Output:  0.9999644161002607
Output:  0.9998789452350273
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  0.9982648614246443
Output:  0.9999725390970704
Output:  0.9998685185697469
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.9975292451866437
Output:  0.9999561877889193
Output:  0.9998711085282457
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  0.9994637652328076
Output:  0.9999979351298913
Output:  0.9999790350862079
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.996607467649978
Output:  0.9999320764847753
Output:  0.9999000313956359
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9952842896014441
Output:  0.9998736010314134
Output:  0.9998272220183582
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9971799277101259
Output:  0.9999374887796665
Output:  0.9999031916960732
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9945232657850906
Output:  0.9997758269883383
Output:  0.9997191653553235
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  0.9993519920335376
Output:  0.9999930687224088
Output:  0.9999568792901335
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.9969697876402703
Output:  0.9999388817132933
Output:  0.9998260723394742
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  0.9996445100304051
Output:  0.9999982520228722
Output:  0.9999844282506594
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  0.9992207059484414
Output:  0.9999933097138365
Output:  0.9999574494446095
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  0.999777890276683
Output:  0.9999990376665991
Output:  0.9999908843118598
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.9984939432939174
Output:  0.9999693889811528
Output:  0.9998895900491124
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.9971013514687176
Output:  0.9999405726754469
Output:  0.9998181068160209
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  0.999429724095685
Output:  0.9999960022452703
Output:  0.9999701888756894
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  0.9987878168147479
Output:  0.9999789741320525
Output:  0.999906417198459
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.9974976956549149
Output:  0.999958823612466
Output:  0.9998738560592336
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9948955531907614
Output:  0.9998701578092712
Output:  0.9998257959738002
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9932533407419464
Output:  0.9997471798661477
Output:  0.9996923953277517
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9924490776187259
Output:  0.9997267209845193
Output:  0.9996692758247688
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  0.9985580601771678
Output:  0.9999750293053511
Output:  0.99988431265782
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.9978773504428082
Output:  0.9999614450958928
Output:  0.9998760431789739
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9917047113209108
Output:  0.9996051934237149
Output:  0.9995431461481038
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.995741216245414
Output:  0.9998863290411483
Output:  0.9998247507276673
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.9951601421114024
Output:  0.9998795338304537
Output:  0.9997231829388786
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9929556608005018
Output:  0.9996580989360744
Output:  0.9996054222191239
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.9984378258051073
Output:  0.9999778780188014
Output:  0.9999142006638051
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9972289960177371
Output:  0.9999187200788625
Output:  0.9998944368758643
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  0.9987616564648399
Output:  0.9999834668205828
Output:  0.9999248851808897
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9953250023645784
Output:  0.9999066925775988
Output:  0.9998584454334862
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.996284002275313
Output:  0.9999160619644362
Output:  0.9998822381134295
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9933602203701717
Output:  0.9997972032134983
Output:  0.999729591324871
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.9963243249250857
Output:  0.9999203374195043
Output:  0.9997914784197123
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  0.9994235578167284
Output:  0.9999961544309709
Output:  0.9999704451071252
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.9984703750574132
Output:  0.9999858070508294
Output:  0.9999388730313319
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  0.999090557179489
Output:  0.9999887465050884
Output:  0.9999394268938554
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.998934013375292
Output:  0.9999841734856085
Output:  0.9999294097940542
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  0.9993818702449024
Output:  0.9999962313899852
Output:  0.9999721962460442
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  0.999143424524206
Output:  0.9999912317801974
Output:  0.9999517767437309
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.9982599199276867
Output:  0.9999654331858987
Output:  0.9998915834579494
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  0.9991863613274102
Output:  0.9999944462115266
Output:  0.9999637971535016
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9906255726508272
Output:  0.9995175937547868
Output:  0.9994834428182147
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9949662528960703
Output:  0.9998572570415111
Output:  0.9998105581357645
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9950462829403355
Output:  0.9998594144323995
Output:  0.9998123476914771
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.9964341646066543
Output:  0.9999473192776444
Output:  0.9998425520185099
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9949767201338457
Output:  0.9998445993260874
Output:  0.9997962020229357
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9952862876507598
Output:  0.9998636880490311
Output:  0.9998048609872368
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  0.9985368396822644
Output:  0.9999850793348061
Output:  0.9999273468621317
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9932135214496779
Output:  0.9997119891588132
Output:  0.9996468605178531
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.9989978239366547
Output:  0.9999927364358456
Output:  0.9999649196865321
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  0.9992241794113254
Output:  0.9999952213412364
Output:  0.9999687404533756
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9968222141160389
Output:  0.999951673689764
Output:  0.9999301195650033
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9961874325361997
Output:  0.9998984494156976
Output:  0.9998543029376078
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9955310922197012
Output:  0.9998625216938072
Output:  0.999822292542485
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.9940650777611111
Output:  0.9998184799630052
Output:  0.9995766548693668
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.9990058000491242
Output:  0.9999887445561271
Output:  0.9999507550847341
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  0.9994614174160573
Output:  0.9999965565656878
Output:  0.9999769014286064
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.9983445515623122
Output:  0.9999827606609483
Output:  0.9999353121795048
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  0.9991377129397226
Output:  0.9999925992845194
Output:  0.9999585060656253
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.9978715437181627
Output:  0.9999735320871874
Output:  0.9999097977337567
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.9981639055849303
Output:  0.9999630778003744
Output:  0.9998834423629492
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  0.9987934376111649
Output:  0.9999881655555303
Output:  0.999935401324531
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9936841820172816
Output:  0.9997692930717326
Output:  0.9997033185110483
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  0.9988234011056114
Output:  0.9999853159252364
Output:  0.9999310695677522
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  0.9985934807457284
Output:  0.9999785262822833
Output:  0.9999056152741473
Epoch: 0 RMSE = 0.8160021168725456
Epoch: 100 RMSE = 0.6642691062715014
Epoch: 200 RMSE = 0.6620308204007155
Epoch: 300 RMSE = 0.6616982265683476
Epoch: 400 RMSE = 0.6615097248598266
Epoch: 500 RMSE = 0.6612852869859758
Epoch: 600 RMSE = 0.6605958822089156
Epoch: 700 RMSE = 0.4819408789960632
Epoch: 800 RMSE = 0.45869415029869
Epoch: 900 RMSE = 0.4361229843771868
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  0.0006148698198997233
Output:  0.9999589232447346
Output:  0.832544613402299
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.16544057220023473
Output:  0.9999239758881364
Output:  0.0210323432998184
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.060073271015170904
Output:  0.9999182079703269
Output:  0.052140284079020466
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9831512849046354
Output:  0.999556526967116
Output:  0.12588306747524386
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9291256935033154
Output:  0.9974770342025018
Output:  0.024946873003834857
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  0.0005813532510538787
Output:  0.9999927658889426
Output:  0.9695356649015566
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  0.0003769532927517941
Output:  0.999992671134338
Output:  0.9714168561663343
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9561308366443233
Output:  0.9992369436384524
Output:  0.05952152695640575
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9370287468836942
Output:  0.9986651445766351
Output:  0.03586863779438565
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.011940914820161862
Output:  0.9998490370522207
Output:  0.10544661960634638
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9079580945465945
Output:  0.9987995963725136
Output:  0.027441756626062526
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.928288645780031
Output:  0.9985597559178444
Output:  0.03290286453712163
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.02342390815339918
Output:  0.9998524447356227
Output:  0.0595559546450632
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9649451812290598
Output:  0.9996658583151775
Output:  0.08930430627212434
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.021359507045430676
Output:  0.999873978538257
Output:  0.0784228733105917
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  0.0002288782397921309
Output:  0.999880053327242
Output:  0.7074331966585067
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.10091365288426717
Output:  0.9999689081776116
Output:  0.08486727170120392
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9298778103055572
Output:  0.998210487400793
Output:  0.02707291890602243
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  0.0011162485005773433
Output:  0.9999936677526836
Output:  0.9626264847708382
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9676197308957682
Output:  0.9994639281315347
Output:  0.0778111878959231
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9862649109408048
Output:  0.9998145280910692
Output:  0.20635291626692323
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  0.0006365179668943855
Output:  0.9999756256698814
Output:  0.8865742069601275
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  0.0005560517259761964
Output:  0.9999934618840484
Output:  0.9682058187124847
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.16271648876192582
Output:  0.9997355188725431
Output:  0.0064517414603945215
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  0.0006217715219955409
Output:  0.9999863722335744
Output:  0.9371581367290275
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.06530248679323675
Output:  0.9998967276299867
Output:  0.03577191257701227
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  0.000580477165864106
Output:  0.9999793862543308
Output:  0.9224025043271427
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9560732627129082
Output:  0.9993039439466621
Output:  0.06495581028039524
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9839492241976174
Output:  0.9997330073298382
Output:  0.1967842323346975
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.047490888265578554
Output:  0.9993383623433426
Output:  0.006251140748381519
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9299756653339551
Output:  0.9988137044005703
Output:  0.03578019608656648
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  0.0010331694190113614
Output:  0.9999823423792569
Output:  0.8760739068761338
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9679189405417375
Output:  0.9994463222641929
Output:  0.0757662488969701
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.966058173083502
Output:  0.9988009235832317
Output:  0.05701035418658697
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  0.00024408128749958864
Output:  0.9999197709165235
Output:  0.8131636437474015
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.1155334620964466
Output:  0.9998493376700086
Output:  0.017512884560195913
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.18922219985069125
Output:  0.9999545266006582
Output:  0.0328834899806028
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9521900983004581
Output:  0.9994612129248154
Output:  0.06087210451322953
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.10638606534265287
Output:  0.999948247378892
Output:  0.05215929859839907
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  0.0002795623423828972
Output:  0.9999574217582742
Output:  0.879034094903519
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  0.00024268125939034508
Output:  0.9999684940224592
Output:  0.9192431237512322
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.08209693399226477
Output:  0.9998086881170734
Output:  0.0167778397133411
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9034669197033405
Output:  0.9985062854231154
Output:  0.02370688957866972
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9348993975578608
Output:  0.9995473933882811
Output:  0.04684004499110353
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9528720447464043
Output:  0.9993253207719243
Output:  0.05988197291782366
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  0.0004102302880040869
Output:  0.9999215730425123
Output:  0.7604891514469495
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  0.00046174060634976974
Output:  0.9999922047863132
Output:  0.9699988953980738
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9672447080720892
Output:  0.9995035997646757
Output:  0.09821658675518335
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9731362029345426
Output:  0.9996313168951937
Output:  0.11300973872470521
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9315805686255371
Output:  0.998824869113204
Output:  0.03231150111310008
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9301628238139601
Output:  0.9988129502839896
Output:  0.035640363664506035
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  0.00039605051687903047
Output:  0.9999235381158849
Output:  0.7839671408947454
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.019398966462530864
Output:  0.9999415835796552
Output:  0.14029673845557325
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  0.0002840567437145156
Output:  0.9999096491935741
Output:  0.7716220967304839
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.1531090630303707
Output:  0.9998051190126934
Output:  0.00899656474220111
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  0.0005024042111272411
Output:  0.9999862650768536
Output:  0.9438546637190468
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.026288235641315667
Output:  0.9998992266978045
Output:  0.07997035866545465
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.949383389682079
Output:  0.9992517531049803
Output:  0.054127322956182236
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.11162827483268162
Output:  0.9994621063570613
Output:  0.004187477434588871
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  0.0009263139168052297
Output:  0.99998313110138
Output:  0.875117159975103
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.02174045392712905
Output:  0.9997777200922847
Output:  0.030339372548526485
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  0.0016587292544776716
Output:  0.9999443231691051
Output:  0.5998394622656777
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.028109632047239232
Output:  0.9999537353186871
Output:  0.17605747825703966
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0032627131316492223
Output:  0.9997881082052553
Output:  0.17291351810895456
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.08279177893518327
Output:  0.9998850866085844
Output:  0.02432059161695251
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.0058542665859061755
Output:  0.9997604383635378
Output:  0.08727626471908086
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  0.00045408207439092947
Output:  0.9999856933858092
Output:  0.950881041671904
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  0.0006329502804095818
Output:  0.9999679633373711
Output:  0.8650053336232264
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9137249808551078
Output:  0.999289823989351
Output:  0.0358858214792254
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9305758192395988
Output:  0.9988123670006194
Output:  0.0360848069412489
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  0.001437043458376178
Output:  0.9999722855651829
Output:  0.786321058605716
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  0.00013566308785673705
Output:  0.9999022155866979
Output:  0.829190863496828
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.88962747599923
Output:  0.9994140917932022
Output:  0.03176165402813052
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.8751980561754649
Output:  0.9993678539189306
Output:  0.02916602858757544
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  0.00021024264444988197
Output:  0.9999654990903568
Output:  0.9184792774272459
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  0.0009497725632218059
Output:  0.9999382314759611
Output:  0.6845838812593885
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  0.0004446379322191102
Output:  0.9999751251977415
Output:  0.9261241216005683
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  0.0007148811700590798
Output:  0.9999875377622269
Output:  0.9483568505662852
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9511605782881979
Output:  0.9991721905894669
Output:  0.052251782217087615
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  0.0002971931381806195
Output:  0.9999458930511271
Output:  0.8423610766034034
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9718757699449848
Output:  0.9995446041874527
Output:  0.10135798179137871
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.003106537430487656
Output:  0.9999138370116633
Output:  0.36891444732063183
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.030872128502584216
Output:  0.9998377799857473
Output:  0.04215645690440255
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9856528319670904
Output:  0.9997016198106715
Output:  0.17398362843624215
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.03907381007190901
Output:  0.9996579486311603
Output:  0.014905866832569304
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.06601921236422613
Output:  0.9998416724762239
Output:  0.02624775873726447
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  0.0004380439328938747
Output:  0.9999862493103082
Output:  0.9530192511956739
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9404220647499134
Output:  0.9995041048213743
Output:  0.061730796602204256
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.05934166612356036
Output:  0.9998223323505424
Output:  0.0215219861850449
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9642705071901032
Output:  0.9992614990360961
Output:  0.06688332585473131
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9034138746159406
Output:  0.9989403402574762
Output:  0.03021532246097778
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  0.000459262433847404
Output:  0.9999869548343485
Output:  0.9558602806411347
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9703827913261489
Output:  0.999498063495826
Output:  0.0914083161078957
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0032597914465114803
Output:  0.9992703276218206
Output:  0.04113852712525592
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.06289207539215048
Output:  0.9999100569605213
Output:  0.043375763368003174
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.02539744565434869
Output:  0.999742034993556
Output:  0.028236115746263942
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0024609652484177567
Output:  0.9999394156511185
Output:  0.5357747062152605
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9182634087316748
Output:  0.9987688943050901
Output:  0.03259235854020016
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  0.0002052367226075054
Output:  0.9999431268989774
Output:  0.8631795112494468
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  0.004106589294336975
Output:  0.9999388038788047
Output:  0.3906091746090325
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9087874785683415
Output:  0.9979442842552948
Output:  0.021938424252429308
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.034210632858416766
Output:  0.9993270255907376
Output:  0.009184548924205062
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0022787309091467675
Output:  0.9999679787396565
Output:  0.6740624289107795
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  0.0007299664893455769
Output:  0.9999796274714111
Output:  0.886725943980094
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  0.003395078739553524
Output:  0.9999964386767982
Output:  0.961472584428095
Epoch: 1000 RMSE = 0.4230701854608874
Epoch: 1100 RMSE = 0.4175112419685536
Epoch: 1200 RMSE = 0.41485425096235107
Epoch: 1300 RMSE = 0.4103578955680538
Epoch: 1400 RMSE = 0.40909818822826494
Epoch: 1500 RMSE = 0.41082801420832915
Epoch: 1600 RMSE = 0.24405718808043136
Epoch: 1700 RMSE = 0.10749263840567606
Epoch: 1800 RMSE = 0.0744351377191831
Epoch: 1900 RMSE = 0.06767195845923742
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  1.875244535913125e-05
Output:  0.029290499329464263
Output:  0.9932405652854469
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.02542385655677871
Output:  0.9682784938614253
Output:  0.004124611907327184
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  1.1324693896142396e-05
Output:  0.01882207200626876
Output:  0.9903522243097874
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9847053228285657
Output:  0.056031266934361196
Output:  0.03166569099797257
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9673285056725566
Output:  0.029199651442458074
Output:  0.014669793376852073
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01315546572299331
Output:  0.9559791020212102
Output:  0.018130716807903655
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  1.666862508522316e-05
Output:  0.04326021511994844
Output:  0.9951528822329743
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.025128875974611765
Output:  0.9686996472649193
Output:  0.004152467693228477
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9660773640705368
Output:  0.023200788425442306
Output:  0.01254180965980519
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.02724188612687963
Output:  0.9809143571447184
Output:  0.005905006553700145
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.0173748322656772
Output:  0.9527056533248622
Output:  0.003430094551900166
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  1.792859528616255e-05
Output:  0.04423228168084798
Output:  0.9950932067558456
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  9.267933763750588e-06
Output:  0.014592689707414914
Output:  0.9886629494081828
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  7.805438165754313e-06
Output:  0.007689251065340556
Output:  0.9817993412404091
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9770076010791449
Output:  0.03897561193264087
Output:  0.021864693116078037
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0020431273360852504
Output:  0.8413643361646755
Output:  0.3015593861745083
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.02334750601564577
Output:  0.9839708300208535
Output:  0.0137371933524246
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9711416348879314
Output:  0.05742699875547706
Output:  0.021643611072812586
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  2.119551296738926e-05
Output:  0.07213256638546307
Output:  0.9966740916248473
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9762894228718874
Output:  0.026493788966159785
Output:  0.01816920333714456
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  0.0002529643469048772
Output:  0.35085240445052
Output:  0.8419172232582575
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.003454662544503816
Output:  0.7542508869698612
Output:  0.0504788943370284
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.03425911908333334
Output:  0.9876071593643796
Output:  0.008097817759203587
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  1.9575862738968487e-05
Output:  0.08554379502689818
Output:  0.9971347237449338
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.03081968205190102
Output:  0.9734308052437787
Output:  0.00459616509710362
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  9.833444252663149e-06
Output:  0.017168504457338127
Output:  0.9900992394432121
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9758245539343576
Output:  0.04700112521050628
Output:  0.021945733032821307
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  1.064326133072977e-05
Output:  0.010900541532524267
Output:  0.977507610824558
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.01321417741232324
Output:  0.9542644724829761
Output:  0.004234521940384007
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.023306415438092323
Output:  0.9732405320929374
Output:  0.009450692897233985
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9743471637701975
Output:  0.027936556983604408
Output:  0.015911686150372945
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9651596088403032
Output:  0.023174292146709238
Output:  0.013679666771895404
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9693291992260259
Output:  0.027974707410117414
Output:  0.01594506369669771
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  2.02488369879861e-05
Output:  0.049801707880161646
Output:  0.9919265954862725
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9889791511840964
Output:  0.09823720869709593
Output:  0.05664568742253738
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  8.555628380843179e-06
Output:  0.010514229648956649
Output:  0.9843420309496806
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.016101056997259472
Output:  0.9428453594699122
Output:  0.0026361312300971253
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  1.8867712290634062e-05
Output:  0.04244552638276837
Output:  0.9948416654004842
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  6.022829818149903e-05
Output:  0.18101567011525657
Output:  0.9979874405186862
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9693309873433491
Output:  0.027922895720559407
Output:  0.015942843198317395
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9786790620529531
Output:  0.04653170867066889
Output:  0.025654775494414656
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.04755623061068184
Output:  0.9939973176252205
Output:  0.016919929839219888
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  9.443095908278677e-06
Output:  0.00845709377157394
Output:  0.9830004833985948
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  1.8911415138953147e-05
Output:  0.05468041138560116
Output:  0.9915560881262822
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.030660666902709608
Output:  0.9809869714097937
Output:  0.006576144702460108
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.01111246697835966
Output:  0.9264424693135078
Output:  0.01748979629000733
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.024460556248627162
Output:  0.9700052652043514
Output:  0.004688937265758621
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9777758177763197
Output:  0.04119021127338823
Output:  0.02367616891964616
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9599923156261705
Output:  0.01305398654626091
Output:  0.009168209719622305
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  1.4883972007476938e-05
Output:  0.026509981520069104
Output:  0.9920406570076873
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9679478611894483
Output:  0.018564896285320643
Output:  0.011586208104994592
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0046100132444703195
Output:  0.8103138942787614
Output:  0.019656651676392137
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9778346579108856
Output:  0.06344651272023559
Output:  0.03053255662273306
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  3.1562951796036585e-05
Output:  0.09175831335685201
Output:  0.9971639688204242
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9843992496954077
Output:  0.07235048956371196
Output:  0.031594783151980076
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9696877848505978
Output:  0.02444441514695236
Output:  0.014790686124137762
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  1.3291362543934302e-05
Output:  0.020490631550529114
Output:  0.9768236743190643
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  0.00012309536872300538
Output:  0.15001945216155838
Output:  0.8215866185079534
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.006927976445595483
Output:  0.8846540022535226
Output:  0.009070671972745217
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9841539639862406
Output:  0.057565955791196874
Output:  0.03189393212095399
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  1.8441228592296827e-05
Output:  0.04480003078768342
Output:  0.9954519406945237
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  1.9973495539010948e-05
Output:  0.07514485607716041
Output:  0.9963791074816386
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  7.718043340500842e-06
Output:  0.00691012854811647
Output:  0.9798022581285639
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0009198287460163809
Output:  0.5495751257171457
Output:  0.38006529443928716
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.02376836956367279
Output:  0.9712839146851998
Output:  0.004100413143424614
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.044422420336135776
Output:  0.9927719263603934
Output:  0.011700082360794834
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  2.3970201124967e-05
Output:  0.07849084906745882
Output:  0.9968378804199314
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9649843141321329
Output:  0.027341460533778776
Output:  0.014882130781157136
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9693423471397403
Output:  0.028052536021318457
Output:  0.015889986207861997
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9824248651823446
Output:  0.057904048257702914
Output:  0.029823220730018828
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.0386106467667059
Output:  0.9858022783392155
Output:  0.007271034409116798
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  0.0013995960305358238
Output:  0.6963435537930532
Output:  0.26166467390649567
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9867218053615819
Output:  0.08969131620655171
Output:  0.043944385858633674
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  2.4890125834682115e-05
Output:  0.057356914723819256
Output:  0.9950066296421862
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.016388638352352134
Output:  0.9056587337839489
Output:  0.002064329823517972
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  1.3673637668020405e-05
Output:  0.03013416110383206
Output:  0.9936101624927095
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9835681034279046
Output:  0.06682370331977873
Output:  0.03732569252832036
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  1.7276077228600378e-05
Output:  0.024558826715404946
Output:  0.9923015910808268
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9880200796030911
Output:  0.06798571362044899
Output:  0.041720451748417035
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9803847446125524
Output:  0.042386816568034134
Output:  0.025287557740705072
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9608905155276228
Output:  0.016559772265708147
Output:  0.00998451888511214
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9762886846036568
Output:  0.05796510652369905
Output:  0.02381221263742731
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9794502060488202
Output:  0.06132025406825476
Output:  0.03490776682632458
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.011954930603989876
Output:  0.8883529814756655
Output:  0.0017109884973586149
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9774299390739287
Output:  0.04240871344327837
Output:  0.023695500433872505
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.04077888083700173
Output:  0.988858612873104
Output:  0.014698330282834354
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.044462326958660814
Output:  0.9907610704337281
Output:  0.011132969735806715
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  1.8884211662363506e-05
Output:  0.04021021122193251
Output:  0.9948773956654726
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  4.960688033953679e-06
Output:  0.005121801835804736
Output:  0.9766456759559206
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  1.421699993810463e-05
Output:  0.021180477292122284
Output:  0.9906480316702158
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  6.200845391012564e-06
Output:  0.006060355956092384
Output:  0.9779403276553011
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.013330805597196222
Output:  0.8881193520097683
Output:  0.0016453619503390212
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9653421204428554
Output:  0.03288134760212545
Output:  0.01601220732941987
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9912784278261992
Output:  0.1477946000712215
Output:  0.07782812522061681
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9864198139989634
Output:  0.10799399092140655
Output:  0.06184909477369082
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.00520443652010891
Output:  0.8508910830379505
Output:  0.030615495439916703
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9772844911377784
Output:  0.04497147677174343
Output:  0.025667079097248784
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.03139651475795613
Output:  0.9838690244686503
Output:  0.007407959168127308
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.002017534471284117
Output:  0.5782631535222541
Output:  0.007377456996967467
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  5.7835692265119914e-05
Output:  0.0697285092687453
Output:  0.9086596490875858
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.020689618498794474
Output:  0.955890927342344
Output:  0.0035023077629116697
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9851009638844542
Output:  0.08072497233663752
Output:  0.043718104239948
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.03247247309206304
Output:  0.9752554372573018
Output:  0.004944486109454553
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  1.2238722643144003e-05
Output:  0.015298573573003597
Output:  0.9893593291355692
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9833202419109299
Output:  0.06129705409356826
Output:  0.03448106457220488
Epoch: 2000 RMSE = 0.05641435378255671
Epoch: 2100 RMSE = 0.04544156457186286
Epoch: 2200 RMSE = 0.04411247663615963
Epoch: 2300 RMSE = 0.038228906978127156
Epoch: 2400 RMSE = 0.03551114865854525
Epoch: 2500 RMSE = 0.03337288191545294
Epoch: 2600 RMSE = 0.03432675514623317
Epoch: 2700 RMSE = 0.03203561782394641
Epoch: 2800 RMSE = 0.030651347164940716
Epoch: 2900 RMSE = 0.029198587158203063
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9910045937825336
Output:  0.04665285983738787
Output:  0.03135666215356615
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  5.516324816511906e-06
Output:  0.0032515669011551193
Output:  0.9855997558557189
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  4.721080342856445e-05
Output:  0.060107703115995594
Output:  0.8787216952214648
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  8.639490188749764e-06
Output:  0.010253460712734155
Output:  0.9933227438289823
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  6.0203117868444e-06
Output:  0.006928453261027686
Output:  0.9911790794360241
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9753242583330971
Output:  0.01283684508260199
Output:  0.008168718934918067
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9902549272183958
Output:  0.03180644329656559
Output:  0.02289583149935555
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9888780761723763
Output:  0.0519102110349519
Output:  0.034216598846386344
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  8.98011189775165e-06
Output:  0.018056118549180333
Output:  0.9942508412984243
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  1.1573468242629673e-05
Output:  0.01661728801087191
Output:  0.9954095486361249
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.008879209926960535
Output:  0.9820514334101352
Output:  0.0027613260876100487
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9818201618485811
Output:  0.02058149240138172
Output:  0.014072315782060118
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  2.4662960414647213e-05
Output:  0.0292568169980498
Output:  0.9416127014165265
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.020782657015119325
Output:  0.9928549415752354
Output:  0.004275894084413862
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  1.135723939233359e-05
Output:  0.011725854230330582
Output:  0.9940182080201249
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9792638014385504
Output:  0.025081490751384505
Output:  0.012336422143021875
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9821267774425089
Output:  0.01927896049540153
Output:  0.013020890893374121
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0010639005168595864
Output:  0.7387641031411001
Output:  0.20845269738307504
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.019881765527660376
Output:  0.9895235457544116
Output:  0.003124616764824856
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9873320888776889
Output:  0.02650274295165668
Output:  0.017534891001066078
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  1.1376032122395048e-05
Output:  0.01998939462018121
Output:  0.9933425742923016
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  3.8051151708697258e-06
Output:  0.0024715464722947097
Output:  0.9800938674359422
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  7.432598759254521e-06
Output:  0.006155330579102017
Output:  0.9905045575663919
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  8.462873971860644e-06
Output:  0.012677971479592973
Output:  0.9941759556159525
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  4.740471318581821e-06
Output:  0.003066980695125764
Output:  0.9837580178518845
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9759900914078521
Output:  0.01098231866882756
Output:  0.008113360049309891
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.02093871226150141
Output:  0.9901962486197405
Output:  0.0033499374043687653
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  1.1198962120908175e-05
Output:  0.01840634539508822
Output:  0.9959704543064544
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9861245322191925
Output:  0.026371288356656985
Output:  0.016523324733854924
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  4.663830730237271e-06
Output:  0.0027696714726577975
Output:  0.9821532801069665
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01735767253605318
Output:  0.991291936907907
Output:  0.00570222545644547
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  5.856856946003377e-06
Output:  0.004121150129049712
Output:  0.9818237995080978
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.01033266785365916
Output:  0.9770671100914127
Output:  0.001779167201937238
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0066988364228064146
Output:  0.9819609732358715
Output:  0.05072771226004624
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9726563584295367
Output:  0.010351659681037115
Output:  0.0075178365941818695
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9826609209393486
Output:  0.028967528678219792
Output:  0.01690818821990045
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  6.745727375120977e-06
Output:  0.007459320596517122
Output:  0.98266600695803
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  5.589840977668266e-06
Output:  0.0058140737709885815
Output:  0.9899348843990062
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  1.991835085318405e-05
Output:  0.034941636232472484
Output:  0.9938350592931229
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9760087068035433
Output:  0.012513971249161702
Output:  0.008778972613791791
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.008667155981640747
Output:  0.9539876958221059
Output:  0.0010832337089675377
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9806897108570679
Output:  0.012053227001051128
Output:  0.009869378897423517
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.007041698842337673
Output:  0.9589428490371728
Output:  0.005473212596014238
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  1.0129521571488782e-05
Output:  0.01765197169152955
Output:  0.9956664236104386
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.02439828095349737
Output:  0.9941898716012415
Output:  0.00514636562382137
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.003979239231265101
Output:  0.914172229713571
Output:  0.0014917642380484636
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  1.1935919814391703e-05
Output:  0.0360898073950874
Output:  0.9974435918668901
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9816851054140411
Output:  0.020962342780560753
Output:  0.01222370361610588
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.03393222064974433
Output:  0.9978859180906136
Output:  0.010454060777365786
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  3.562674100710987e-05
Output:  0.0817589807351664
Output:  0.9982517404859711
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9818516294085593
Output:  0.017598877202305376
Output:  0.011980969188315694
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  1.2261114675305132e-05
Output:  0.031799883394864475
Output:  0.9967459024442635
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9879326231188857
Output:  0.03785778120255006
Output:  0.023995481576368858
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.019947737960309447
Output:  0.9919852917373101
Output:  0.004748178608478762
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9696582288094626
Output:  0.007365757387113448
Output:  0.0054840111626738896
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.011182683485697651
Output:  0.9743500735879581
Output:  0.006324983122178291
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9833421664944676
Output:  0.028582228351472578
Output:  0.01907955434738235
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  1.8916691987288756e-05
Output:  0.038334267823760364
Output:  0.9975227090746184
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.03022561470175471
Output:  0.9965960291441431
Output:  0.007164975555852702
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.00796402776570342
Output:  0.9554430479880904
Output:  0.0010942504600438413
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  3.027792284514407e-06
Output:  0.002080132857974943
Output:  0.9789707883935679
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  9.634860815372183e-06
Output:  0.010121946348097986
Output:  0.9904851165089519
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9741378955663608
Output:  0.010223249053727772
Output:  0.00693493138677809
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.012947082963814829
Output:  0.9813308529399712
Output:  0.002427630229082784
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  0.00013622236252388065
Output:  0.25702531858804434
Output:  0.854948151286573
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.015959117242349257
Output:  0.9868253734083884
Output:  0.0028689186891635264
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9799629331105592
Output:  0.012449134182491562
Output:  0.00876458841701461
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.01734664635188207
Output:  0.992359431693574
Output:  0.004042453118927753
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9865918008471466
Output:  0.028258967329097277
Output:  0.01890868117535916
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  3.129413439608712e-05
Output:  0.03835529781516122
Output:  0.9305986143382955
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9727445026932534
Output:  0.012126180220650963
Output:  0.008245000576657177
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9760087843963345
Output:  0.012482283896221686
Output:  0.008788032822224323
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9825480169467091
Output:  0.025716677934332743
Output:  0.013388795002805712
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.03401982106881789
Output:  0.9966705940280755
Output:  0.00757169956298286
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  5.244935175442702e-06
Output:  0.004224516692563316
Output:  0.9860146502956633
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.01592627822524525
Output:  0.9873565494485662
Output:  0.0028477222718659287
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.007036762970705222
Output:  0.9661789768890836
Output:  0.0038494475490298188
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9748243306216917
Output:  0.008265271600961332
Output:  0.006364705406603135
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  6.940574550367189e-06
Output:  0.007568156599800128
Output:  0.9913169952813904
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.011779199987327899
Output:  0.9819635393773651
Output:  0.00218231635513543
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9929047017210728
Output:  0.07243032228520536
Output:  0.04338049749407646
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.021145985088884055
Output:  0.9939607213092368
Output:  0.004792237492775458
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.012102235154706443
Output:  0.9801672458147614
Output:  0.006984649032602859
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9883370489079262
Output:  0.0324780515264568
Output:  0.017780126130482875
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  1.0609378608455484e-05
Output:  0.01015958565598007
Output:  0.9930391302949398
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9822078284916801
Output:  0.018744065550212054
Output:  0.012980801410501426
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9895395961361839
Output:  0.041777370964619275
Output:  0.024340980488940595
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9680299342766162
Output:  0.005835249014229064
Output:  0.00500359543581861
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.014516538911402059
Output:  0.9927420938983446
Output:  0.010016070808359668
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.010433651137532435
Output:  0.9579261021946555
Output:  0.0014239928745872592
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9877911917144575
Output:  0.02561895115261841
Output:  0.017368615223109445
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  1.0782557201925084e-05
Output:  0.017739793354846156
Output:  0.9956733782984973
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  1.2989764100724901e-05
Output:  0.029908564582350635
Output:  0.9970311983480565
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9760095486332174
Output:  0.012478008928046859
Output:  0.008786550937709707
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.011645933933433482
Output:  0.9802258810673891
Output:  0.005558854731353991
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  1.148483019823751e-05
Output:  0.017258485291159406
Output:  0.9954322572054253
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.016519818110625726
Output:  0.9886432026481825
Output:  0.0030361232683394886
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9867690333064023
Output:  0.031044864765132994
Output:  0.020474836358166736
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.014784119998685402
Output:  0.988087115911042
Output:  0.0029098463585706474
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9737967582468647
Output:  0.014570083473331425
Output:  0.008908093726692073
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.021806761397231242
Output:  0.9950557047835499
Output:  0.005600551590332958
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9830309393536826
Output:  0.021178336635700557
Output:  0.014103351159852524
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.027884051612068167
Output:  0.9970431885880375
Output:  0.008340587608560265
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  1.4533284303803601e-05
Output:  0.03222591826893479
Output:  0.9972347115772852
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9842513011588554
Output:  0.019392629320673673
Output:  0.01381088347210792
Epoch: 3000 RMSE = 0.028726707080437428
Epoch: 3100 RMSE = 0.028128112360748917
Epoch: 3200 RMSE = 0.027121044311296413
Epoch: 3300 RMSE = 0.026741209295163815
Epoch: 3400 RMSE = 0.02623823158062122
Epoch: 3500 RMSE = 0.025291529378896376
Epoch: 3600 RMSE = 0.025399490680299716
Epoch: 3700 RMSE = 0.02495300695210361
Epoch: 3800 RMSE = 0.02420882773086798
Epoch: 3900 RMSE = 0.024410452880328472
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  2.4190152042994254e-06
Output:  0.0015091113316954689
Output:  0.9826130968641277
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.977343391223734
Output:  0.00903537721255583
Output:  0.005998439115337902
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.011126749091128478
Output:  0.98847899433111
Output:  0.003585175395961163
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  4.567409108128786e-06
Output:  0.004476561933174478
Output:  0.987970647392293
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.02447283292915369
Output:  0.9976158119319968
Output:  0.005512269275230099
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  9.28901281299686e-06
Output:  0.012243424357977598
Output:  0.9961711591561673
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  8.060483943591295e-06
Output:  0.012702807843304232
Output:  0.9951550325073263
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.979971632926924
Output:  0.008178767155193063
Output:  0.005894935303618979
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  6.999051842520407e-06
Output:  0.006589605992154619
Output:  0.992907742719859
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.017160366383550212
Output:  0.9958108100255999
Output:  0.0036580971584267968
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.007569965058762295
Output:  0.9882284431198247
Output:  0.0019864911560047186
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  9.218251248458518e-06
Output:  0.012730476655683068
Output:  0.9962044411293686
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  4.452850063103746e-06
Output:  0.004206303872021258
Output:  0.9917187185405982
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.017660269927638136
Output:  0.9965635829618918
Output:  0.004285606395457436
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  7.556411211498349e-06
Output:  0.01435387804337564
Output:  0.9948818791346493
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.008316201118539425
Output:  0.9838342569247976
Output:  0.0013654486457848425
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9800398190822963
Output:  0.009308815947977691
Output:  0.006391813632353353
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.01044460238172036
Output:  0.9867906641462371
Output:  0.0018600945432688213
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9783565855374401
Output:  0.010832002719312778
Output:  0.006497212383855771
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.011955700255337435
Output:  0.9917050855063998
Output:  0.0022231767907359987
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  4.424996586307059e-06
Output:  0.002385447321633385
Output:  0.9879916833564416
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.988791156217384
Output:  0.021237893914545135
Output:  0.01376542071172939
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.006656399087013809
Output:  0.9798892553026909
Output:  0.0025113471691552897
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9732553221257984
Output:  0.004356068691224796
Output:  0.0036312838144616686
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  9.841716761813596e-06
Output:  0.023383526394456646
Output:  0.9973041720308988
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  5.905997495442548e-06
Output:  0.004442845005689157
Output:  0.9921878240524135
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9796279870187552
Output:  0.009530965421096363
Output:  0.005945642229025742
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  4.210428149743595e-06
Output:  0.0031044750872565134
Output:  0.9883584018858242
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9851016834488987
Output:  0.014425629347536937
Output:  0.009456149841837031
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.004652950641027874
Output:  0.9599212215452098
Output:  0.00556659275300313
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9918392395349833
Output:  0.023958887246184418
Output:  0.016645313473929425
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.003242798412839597
Output:  0.9718080468169984
Output:  0.07601868543704078
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  9.127463579682216e-06
Output:  0.008646992955794191
Output:  0.9949961007966981
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  8.099847642333577e-06
Output:  0.012869017863705211
Output:  0.9964214632116765
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.016916045106606357
Output:  0.9931264562212389
Output:  0.0025661384410581947
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  6.670128535793288e-06
Output:  0.009083501668873619
Output:  0.9952501287705445
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  8.96644385316168e-06
Output:  0.013450981013276839
Output:  0.9966588390543333
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9851318298201263
Output:  0.014048618537495687
Output:  0.009433836824542
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.028056906856027245
Output:  0.9977283456706745
Output:  0.005699166054481651
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9924626169798622
Output:  0.03528124427637686
Output:  0.022853407727692232
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.022576157287223026
Output:  0.9979422185672532
Output:  0.006393851803279184
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9848793480257387
Output:  0.013123665269973305
Output:  0.008720813065750179
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.013538190533063118
Output:  0.9934625123005584
Output:  0.0046267910206059
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9903984533287685
Output:  0.02422521421741387
Output:  0.012992317446271287
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.017111599161548124
Output:  0.9951296551216418
Output:  0.0031989230471111975
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  3.791131620401828e-06
Output:  0.002229280051953034
Output:  0.9865173571868636
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  6.607317113688204e-05
Output:  0.10478396055856595
Output:  0.8002034529880608
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.006397489581432307
Output:  0.9682557787764055
Output:  0.0008427041167040018
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9800406174140155
Output:  0.009303848468609325
Output:  0.006399998545373616
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.009558310974468768
Output:  0.9874503899951782
Output:  0.0016654363336462063
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  3.0522781162504526e-06
Output:  0.0018002558827356126
Output:  0.9834840190302021
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  8.634390505231129e-06
Output:  0.013036605934916509
Output:  0.9964266308557291
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  3.174539334711777e-05
Output:  0.05654968369064673
Output:  0.9640947429240919
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  6.911499209487969e-06
Output:  0.0075066477170899
Output:  0.9944650650003727
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9747908366165693
Output:  0.005460511739017852
Output:  0.003997939394848545
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9848117264337233
Output:  0.01541452517902797
Output:  0.010231122673625056
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  4.162414130067e-06
Output:  0.0025953166435964013
Output:  0.9867814059125547
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  4.831117479433546e-06
Output:  0.005082160381407757
Output:  0.9926528960636297
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.01603994638259819
Output:  0.9926315765364564
Output:  0.002402098686917619
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9855813175703376
Output:  0.021630217191102256
Output:  0.012342519850572874
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  2.003401209349643e-05
Output:  0.024666159322049717
Output:  0.9463472927197969
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.989808922732895
Output:  0.01922034718714495
Output:  0.012653318098442522
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9898985592566132
Output:  0.028463401322413148
Output:  0.01751418340805334
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.012887599737486781
Output:  0.9907536117029597
Output:  0.0022007813342574257
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.011902047320828819
Output:  0.994851099136889
Output:  0.007755885092183258
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9848726129073011
Output:  0.015550907422292619
Output:  0.008931856259799297
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9790343271141966
Output:  0.006155100122267051
Output:  0.004628444206648406
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9833407938317096
Output:  0.009275150742424578
Output:  0.0063801180152935925
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.983805343396295
Output:  0.009005226726990546
Output:  0.007173950191064805
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9889364988370506
Output:  0.02334740298002179
Output:  0.014922040652395798
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  1.0427208594944933e-05
Output:  0.022101552645135875
Output:  0.9975392902852886
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9912943081858044
Output:  0.031418874831420966
Output:  0.017778372542539327
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  9.564194946300275e-06
Output:  0.026446457078280357
Output:  0.9978909265619966
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.010383958123818031
Output:  0.9865074852405278
Output:  0.0051692030558315215
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9786033607663353
Output:  0.007569472054532506
Output:  0.005060257310410766
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0012272799024529604
Output:  0.834027415805014
Output:  0.13582446730658862
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0029067896611202296
Output:  0.9281316051593843
Output:  0.0013163161942705687
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9800434871086238
Output:  0.009313933406606635
Output:  0.0063916688193336475
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9858389509324177
Output:  0.015882115379734208
Output:  0.010259902181319624
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.01352693394840744
Output:  0.9922119406565825
Output:  0.002292372857438184
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  8.567654692580562e-06
Output:  0.007574350583174588
Output:  0.9941614155664911
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.008469328470624737
Output:  0.969906627234734
Output:  0.001087468665763973
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9772322979666137
Output:  0.007701915456772904
Output:  0.005470813766555434
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  2.6205508191987963e-05
Output:  0.05535735247933866
Output:  0.9986828952667247
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.019604976713353393
Output:  0.9958775684009039
Output:  0.0040007347079228555
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.990673588540284
Output:  0.03935269933548986
Output:  0.024946365002129624
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.988444981957762
Output:  0.01972486497532926
Output:  0.01203097251669903
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  1.5017922170004362e-05
Output:  0.027916251549163638
Output:  0.9979730673423478
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.006976191275319772
Output:  0.9673298567519982
Output:  0.0008300375685755036
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9868363349297824
Output:  0.01455123160723428
Output:  0.010040695033674076
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  1.298228087539256e-05
Output:  0.0203184652201664
Output:  0.995908354781332
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  1.1667521515034788e-05
Output:  0.023890453738368445
Output:  0.9977037280875206
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9894253937863868
Output:  0.019853247810642474
Output:  0.01276164561881032
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  5.5713059551828744e-06
Output:  0.005570828084695751
Output:  0.9927809391548367
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9860497198061333
Output:  0.02145625657223818
Output:  0.013896193372771511
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9856756459624997
Output:  0.01910850222380879
Output:  0.009785079485419547
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.007999752562821441
Output:  0.977594831503352
Output:  0.005835790751855503
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9830664013186504
Output:  0.01858632883017365
Output:  0.00901638058775346
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9940596087360348
Output:  0.05516553698799631
Output:  0.03176334544992333
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.012869177310207267
Output:  0.9911957773958723
Output:  0.0021770757242435116
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.014026008764290311
Output:  0.9946841870925845
Output:  0.003093160861479295
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  3.447912267542233e-05
Output:  0.04866832684901777
Output:  0.9101885176991898
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.015570434828238286
Output:  0.9940516566592762
Output:  0.0038363864621932353
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  3.7144397661163044e-06
Output:  0.0020040303788205036
Output:  0.9852752866489818
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.027300092590686092
Output:  0.9985016814741047
Output:  0.008137837808004797
Epoch: 4000 RMSE = 0.023919428832318325
Epoch: 4100 RMSE = 0.02375195216321429
Epoch: 4200 RMSE = 0.023202883960413905
Epoch: 4300 RMSE = 0.02292153365968873
Epoch: 4400 RMSE = 0.02283312945888525
Epoch: 4500 RMSE = 0.022488150100627283
Epoch: 4600 RMSE = 0.02214786429395924
Epoch: 4700 RMSE = 0.022074105426518185
Epoch: 4800 RMSE = 0.021639380857697225
Epoch: 4900 RMSE = 0.021669497167998177
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9903260803010074
Output:  0.019579203613586952
Output:  0.012014974929563951
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.985393902942119
Output:  0.015417837514568525
Output:  0.0072858810765971
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9801361505359529
Output:  0.006418110388332928
Output:  0.004404815372986278
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9877899108520626
Output:  0.017976846446942394
Output:  0.011194782633311256
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  3.790961260066661e-06
Output:  0.0037045237845546447
Output:  0.9892723737761885
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  7.98560262026132e-06
Output:  0.010536931495801913
Output:  0.9964661683464205
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  3.189256718266909e-06
Output:  0.0017191307713039054
Output:  0.9863986683437315
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.013880093904136304
Output:  0.9942602415628531
Output:  0.0019360001863640826
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9812148934136273
Output:  0.009009498929198324
Output:  0.005239182760540448
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9911627514855146
Output:  0.02389883129205969
Output:  0.014106366974787518
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9780370883618159
Output:  0.0045495859810349894
Output:  0.003214885813266499
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9874327517622321
Output:  0.018087909572014938
Output:  0.009942441587244569
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.009796086402785412
Output:  0.9910794540779997
Output:  0.002867695310391201
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  4.791240576364128e-06
Output:  0.004787646029772464
Output:  0.9933308333426537
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.011111096453478514
Output:  0.9931130408540356
Output:  0.001760097938195439
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  3.823161975114255e-06
Output:  0.0036104299739476093
Output:  0.9923648030764787
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9814027285271608
Output:  0.006302221349974833
Output:  0.004074493863531068
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  1.0034093732007493e-05
Output:  0.02058307066489943
Output:  0.9978794446411334
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.010325838995171017
Output:  0.9935182313691657
Output:  0.0017968790855951665
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.00903569855878663
Output:  0.9896094370214774
Output:  0.001503593247150257
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.007180835991571534
Output:  0.9873531677259763
Output:  0.001102657333429682
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9910989529719791
Output:  0.016094647828741024
Output:  0.010185355813354932
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  2.078020821567019e-06
Output:  0.0012956245730383477
Output:  0.9839490041363051
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  1.0628900886011429e-05
Output:  0.016563316369095422
Output:  0.9964085945729935
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  7.92427302753078e-06
Output:  0.010954618122117706
Output:  0.9964974014405287
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.002652568427356443
Output:  0.9738182503340248
Output:  0.07088937077465719
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  3.797652811299373e-06
Output:  0.002046048298949478
Output:  0.9889243300401094
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9817091721685565
Output:  0.0051348103034309835
Output:  0.003721617866286428
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  5.068899253849505e-06
Output:  0.003812325418582195
Output:  0.9927965452529472
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9826015141423353
Output:  0.007761800681789387
Output:  0.0051463350543802175
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9858164620193767
Output:  0.007538684835152374
Output:  0.005764648103972587
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.024339671145300557
Output:  0.9982314051968774
Output:  0.004602691641584738
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.013761594382244214
Output:  0.9954622512166783
Output:  0.0030312350245561654
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9868662101107728
Output:  0.012959046168880424
Output:  0.0071953613272052455
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0020870217524006627
Output:  0.9349416683995241
Output:  0.05762870806483075
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9802588856969339
Output:  0.007530938122983591
Output:  0.004829496257224114
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9876076152006205
Output:  0.015883793434844577
Output:  0.007897023643401545
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9826020775486973
Output:  0.007763039217167574
Output:  0.005145482417918824
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.005535763173143388
Output:  0.9751373244901019
Output:  0.0006765084166412694
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.002622217679341848
Output:  0.9449953725834955
Output:  0.0010246149522834984
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01204577701444084
Output:  0.9950345110093315
Output:  0.003646230191096232
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  2.6252139488304634e-06
Output:  0.0015507917559252557
Output:  0.984667826643805
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  5.97114314647602e-06
Output:  0.006519760240932096
Output:  0.9948338448065992
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9823201113072774
Output:  0.007928362895028828
Output:  0.004791833565921565
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  5.510251761652785e-05
Output:  0.09861231491004133
Output:  0.8042899810931801
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9918327244828419
Output:  0.033086817733854905
Output:  0.02015679013130659
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  8.967852670758435e-06
Output:  0.019074457110825675
Output:  0.9977305897301478
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.006021123804500407
Output:  0.9742277065358976
Output:  0.0006724087302433634
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.00644458800596113
Output:  0.9905854908065914
Output:  0.0016414427407672588
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.014754216975110361
Output:  0.996181548515274
Output:  0.002603721838821707
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  7.703310879819269e-06
Output:  0.011561966621300072
Output:  0.9969306522480446
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  7.418875062116503e-06
Output:  0.011221112387694715
Output:  0.9967029040629364
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9854798563348792
Output:  0.007738503643781938
Output:  0.005139245101443123
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.021159774480475915
Output:  0.9981377639752461
Output:  0.004473656231835013
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  6.954983867456168e-06
Output:  0.011053213453540541
Output:  0.9967143639065964
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9899188991612626
Output:  0.0164843759832846
Output:  0.009706121459660245
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.015254113101756136
Output:  0.9973154592247558
Output:  0.0034766155458501166
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9916809645800487
Output:  0.02018390687653163
Output:  0.010503977540500158
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.007366958156929074
Output:  0.9760124568827208
Output:  0.0008809408406223824
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9870049437937464
Output:  0.011745517290104803
Output:  0.007605790837811014
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  8.224061146775558e-06
Output:  0.022837465162234123
Output:  0.9980551737095213
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.011141576132966268
Output:  0.9927579188496176
Output:  0.001780518365997363
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9934032594455963
Output:  0.029648163851983027
Output:  0.018463117957440944
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9826014999664398
Output:  0.007760115118537689
Output:  0.005153178986323929
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.01481846087013873
Output:  0.9967257663614386
Output:  0.0029680219691080143
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9924083742599898
Output:  0.02633444813379204
Output:  0.014346616796775924
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.008285991963184948
Output:  0.9902403760067705
Output:  0.00133959108504104
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9867269589313965
Output:  0.01289698628694281
Output:  0.008236576814906721
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  2.6682071598533115e-05
Output:  0.05108867392909592
Output:  0.965877273331117
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9876313377900957
Output:  0.013266336836569236
Output:  0.008272603138363413
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  6.5292861211729805e-06
Output:  0.01013993198153707
Output:  0.9958325926986779
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9928596738366123
Output:  0.02008579198499152
Output:  0.01342897342749361
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.005765882894711485
Output:  0.9766130423704269
Output:  0.0060763038046344545
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  4.15463710484613e-06
Output:  0.00437244800364333
Output:  0.9932245988406039
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  8.4631559294561e-06
Output:  0.02014400322109225
Output:  0.9975196476523074
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  3.545388744053642e-06
Output:  0.0022126243432589367
Output:  0.9878856838554557
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.01082270092382709
Output:  0.996182468607907
Output:  0.005980965472802669
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  3.620373147868445e-06
Output:  0.00266754009462573
Output:  0.9892628206620062
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.014607824318063541
Output:  0.9946244994600476
Output:  0.0020797609145389185
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.023519111866874047
Output:  0.9988203405052314
Output:  0.006637400536273437
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9825126398828977
Output:  0.006823082826860383
Output:  0.004747355789718269
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9869969964658998
Output:  0.012049080899876198
Output:  0.007620076181124685
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.976609333195844
Output:  0.003633644040393289
Output:  0.002922522555100501
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  6.009209677964925e-06
Output:  0.011208541261406151
Output:  0.9956794052918535
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9907621006834084
Output:  0.016606639878609632
Output:  0.010287403336350963
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  7.826701242597541e-06
Output:  0.007408122131145041
Output:  0.9954044223771079
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.012107782156036917
Output:  0.9958393818096098
Output:  0.002505855996286675
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9902029797833466
Output:  0.017781676481541803
Output:  0.011096212575312648
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  1.2853524073172175e-05
Output:  0.023903887566162622
Output:  0.9981413210164575
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9948024840990082
Output:  0.04648320585663366
Output:  0.025688397026011188
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  5.683031381923683e-06
Output:  0.007717897641979537
Output:  0.9956695560719344
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.016753798784573698
Output:  0.9967141112199471
Output:  0.0032935805947935095
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  3.2549056393840026e-06
Output:  0.0019107901048261025
Output:  0.987593203466921
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0033144339918941283
Output:  0.9573260286939832
Output:  0.005898308330198535
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.009688284603547846
Output:  0.9902634717368052
Output:  0.0038781699355661526
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.011653933933541097
Output:  0.9938797261871413
Output:  0.0018620299878089723
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.019514634824800692
Output:  0.9983926351325986
Output:  0.00518538506236326
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9884920385248596
Output:  0.012162462104191188
Output:  0.00808866311972802
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  2.1637382191400547e-05
Output:  0.04554150153124876
Output:  0.9988406646057191
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9868073863860222
Output:  0.010955021512117896
Output:  0.007028992402639572
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  5.767387112842832e-06
Output:  0.005369647885678923
Output:  0.9937656653508288
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  7.230018780402486e-06
Output:  0.00634863354579536
Output:  0.994728236829214
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  1.6937898091816525e-05
Output:  0.022301951137079685
Output:  0.9487486739123896
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.005328933254755186
Output:  0.9822038120140733
Output:  0.0022608721334214568
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  1.7668850439231282e-05
Output:  0.022959344541374705
Output:  0.9509081660114163
Epoch: 5000 RMSE = 0.021051604747644417
Epoch: 5100 RMSE = 0.021324451483168486
Epoch: 5200 RMSE = 0.020788667012523143
Epoch: 5300 RMSE = 0.02070859584425079
Epoch: 5400 RMSE = 0.02066938879638093
Epoch: 5500 RMSE = 0.020517400650046754
Epoch: 5600 RMSE = 0.020510632118639523
Epoch: 5700 RMSE = 0.02029207768264683
Epoch: 5800 RMSE = 0.020063049623036306
Epoch: 5900 RMSE = 0.019850459942044707
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  6.961386669460105e-06
Output:  0.00673876344016009
Output:  0.9955460250862361
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  4.262941220956667e-06
Output:  0.004352890936912982
Output:  0.9935436237633217
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9882412448444086
Output:  0.011338009851821037
Output:  0.006110075050005969
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  6.1868903299735525e-06
Output:  0.010057045652957161
Output:  0.9968099149075804
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.001618699022096526
Output:  0.9605654691700544
Output:  0.0977400033848267
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9953234688637794
Output:  0.04101636301440456
Output:  0.021821184571176277
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  7.317708887247261e-06
Output:  0.02080947620407883
Output:  0.9981093968043316
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  1.760834935182042e-05
Output:  0.025696901332977928
Output:  0.943516164454759
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.012391603881415698
Output:  0.9952372535805439
Output:  0.0016211363325246621
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9869660341521312
Output:  0.0067775922866895105
Output:  0.004352944455218534
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.0066189062715036285
Output:  0.979831829501759
Output:  0.0007361659086175614
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9887198163522082
Output:  0.015862101064610785
Output:  0.00843666978980747
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9842844215516494
Output:  0.005979950077929533
Output:  0.004022320734903061
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  5.123784014719732e-06
Output:  0.004887884199590952
Output:  0.9939528099668978
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.00640530712970173
Output:  0.9894913290725581
Output:  0.0009231077016481174
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.015167448503411297
Output:  0.9973230954655601
Output:  0.0027135710039595416
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9843812487984577
Output:  0.0067966126671026505
Output:  0.004365147220180344
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9843814561896828
Output:  0.0067965883676070335
Output:  0.004365144289099261
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.018919568018239023
Output:  0.998457994065573
Output:  0.003735820118542733
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  4.49827298266463e-06
Output:  0.003454064966717291
Output:  0.9930462246937017
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9926470256244654
Output:  0.029142229705642522
Output:  0.017098153302341254
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.00807915925570389
Output:  0.9913361734283659
Output:  0.0012589853742789262
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9920494059347934
Output:  0.021011454440150016
Output:  0.01196984764360711
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0033398933369344227
Output:  0.9687357773341022
Output:  0.004363658560788932
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9920000496722633
Output:  0.014127089905848248
Output:  0.008639542523020982
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.013220311197221366
Output:  0.9968485759849753
Output:  0.0021664324555603315
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.013626456413806958
Output:  0.9977761380846313
Output:  0.0029032932766527436
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.983186562219481
Output:  0.007874304493246147
Output:  0.004446159149843745
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004937586116741856
Output:  0.9792596479253806
Output:  0.0005668732211277949
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  3.396716042122373e-06
Output:  0.003276298423513597
Output:  0.9926156211799885
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  2.8957812079324986e-06
Output:  0.0017382565097341823
Output:  0.9879622000769742
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  5.34850093070946e-06
Output:  0.010255011069880537
Output:  0.9957924861956285
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9940630341996938
Output:  0.026101361031608455
Output:  0.015658182784828112
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9843813558933657
Output:  0.00679630448510181
Output:  0.004365019078142287
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9896511364340594
Output:  0.01067652419662112
Output:  0.006854861920428249
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.013047147359654272
Output:  0.9955444797937655
Output:  0.0017385602802351347
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  5.053745850790842e-06
Output:  0.007022206814172436
Output:  0.9958006802587402
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9880654056035577
Output:  0.011318177670957857
Output:  0.006976798768304819
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.010444694926417624
Output:  0.9949509716938737
Output:  0.001550009006044009
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9883145152563124
Output:  0.010305779801042685
Output:  0.0064414766499698425
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.005835569509456244
Output:  0.9923287480704731
Output:  0.0013484759454103399
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9889307335273605
Output:  0.013876539810668373
Output:  0.006708855757402651
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.0058381276774485185
Output:  0.983173068246859
Output:  0.00444326997601566
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  7.048049133312515e-06
Output:  0.009961794109169132
Output:  0.9966085901605929
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.008530589281639002
Output:  0.9922459320392761
Output:  0.002497951275416959
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  7.103160983923892e-06
Output:  0.009581117384720018
Output:  0.9965782486721627
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9835724607184955
Output:  0.0044956040580238785
Output:  0.00315557211042346
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.007421564410419669
Output:  0.99194103401452
Output:  0.0011138727540620438
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9821626142221166
Output:  0.005618921662729735
Output:  0.003734649785261909
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  5.813244011750686e-06
Output:  0.00927107067133128
Output:  0.9959366165853628
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.01743601978123852
Output:  0.9986679908997437
Output:  0.0043388445713226295
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.990946048064958
Output:  0.014462532422828685
Output:  0.008224502322060597
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.012104357620925685
Output:  0.996137932345557
Output:  0.0025968002694195884
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  3.1513944604168912e-06
Output:  0.0020157455698929204
Output:  0.9882148235697731
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  6.598451030723614e-06
Output:  0.010212165958229399
Output:  0.9967913803899802
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.009913725790631947
Output:  0.9942856535573414
Output:  0.0014720026354169964
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  7.978679127613187e-06
Output:  0.01737777525620133
Output:  0.9977908058257178
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01024123996120418
Output:  0.9955432287738003
Output:  0.003267073437049775
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9883183771921037
Output:  0.010568057163680452
Output:  0.006454946340857598
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  3.370117288946799e-06
Output:  0.001853987569031892
Output:  0.9892880522449646
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.01081267583554898
Output:  0.9965525064577512
Output:  0.0020922747294782355
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  3.2212527115466133e-06
Output:  0.0024271021779389166
Output:  0.9895627740720521
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9833396696036998
Output:  0.005509654748065694
Output:  0.0034543754867477033
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.005086647325328997
Output:  0.9863519114838349
Output:  0.0017549764220986122
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  5.272638737005854e-06
Output:  0.005867070904010906
Output:  0.995035356977312
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  6.852977469044883e-06
Output:  0.010524380306550708
Output:  0.9970124921757249
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9872292843415288
Output:  0.006616110138797596
Output:  0.004883290650106759
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.02173203777955539
Output:  0.9985313714098359
Output:  0.0038593316548155223
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.013244041737623105
Output:  0.9972901711260953
Output:  0.0024738733924892886
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  2.5544364771144782e-05
Output:  0.0541721734711897
Output:  0.9623111671082204
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9925616563982937
Output:  0.017664372985834828
Output:  0.008905943113551598
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  2.902794722912705e-05
Output:  0.049018737921479864
Output:  0.8843570604485329
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9881501494286566
Output:  0.00960499138352912
Output:  0.0059581840671744535
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9822834515138631
Output:  0.0065889553437279685
Output:  0.004097552106479283
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9802928132985533
Output:  0.0039787182960791985
Output:  0.0027261765586856852
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9913010691149968
Output:  0.01719358181368628
Output:  0.01019358886135308
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  1.8467990503332592e-06
Output:  0.0011753452357864903
Output:  0.9844677641990932
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.009761551094354412
Output:  0.9968405404803447
Output:  0.004988782425962089
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.009210427424721099
Output:  0.9946157580905687
Output:  0.0015054377060223208
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  2.8308977955280586e-06
Output:  0.0015569351529335633
Output:  0.9868587722844526
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9931841846444928
Output:  0.02312833898800523
Output:  0.012167023594473912
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  6.403831124956128e-06
Output:  0.00574395256234468
Output:  0.9949116170129712
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9935751503927882
Output:  0.017657521835832198
Output:  0.011381048171885249
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.008774641162845796
Output:  0.991948768459836
Output:  0.0032265257792804328
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.989013074709351
Output:  0.0157873416157698
Output:  0.00949585055592397
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9869850772697587
Output:  0.013445592357774077
Output:  0.006191089063282359
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9916964241223216
Output:  0.014577906832375517
Output:  0.008721826557695557
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9911900686646067
Output:  0.015616057707507682
Output:  0.009407942494534261
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  8.926927016178456e-06
Output:  0.018728935053772645
Output:  0.997946439527157
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9888838594623933
Output:  0.011637646432892232
Output:  0.007007914043514919
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  1.3618380980488489e-05
Output:  0.018528119519529575
Output:  0.9542944539384451
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  2.33545317093071e-06
Output:  0.0014073177032162773
Output:  0.9851634369869016
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  1.9070583543555134e-05
Output:  0.04109605105824822
Output:  0.9988876890365486
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9789567137755064
Output:  0.00318294691216002
Output:  0.0024755756266329984
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0020397107953100384
Output:  0.943739184701841
Output:  0.0010309535329100221
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9841767146900606
Output:  0.00692433549003388
Output:  0.004068401532248307
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.0053754284909904235
Output:  0.9785083041832011
Output:  0.0005615626770549844
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  3.696679610097566e-06
Output:  0.003976674091716199
Output:  0.9934173505403118
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.021080170625416776
Output:  0.9990249882571988
Output:  0.005543251514075061
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  7.5301301925336955e-06
Output:  0.018347436719793466
Output:  0.9975904415280065
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  3.174176681601435e-06
Output:  0.0031075928144436043
Output:  0.9903190473806145
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.001065630307830411
Output:  0.8787768383761557
Output:  0.09837108977208177
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.00995557852028182
Output:  0.9939833912901544
Output:  0.0014868018937260214
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  1.1438865410261437e-05
Output:  0.021815648182489652
Output:  0.9981951247662311
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  9.10133049177937e-06
Output:  0.014404184099511006
Output:  0.9966633946215362
Epoch: 6000 RMSE = 0.0199527868923786
Epoch: 6100 RMSE = 0.01983600040042202
Epoch: 6200 RMSE = 0.019565907524444235
Epoch: 6300 RMSE = 0.019597945882855475
Epoch: 6400 RMSE = 0.019409603185311392
Epoch: 6500 RMSE = 0.019449129253337815
Epoch: 6600 RMSE = 0.019192783515466834
Epoch: 6700 RMSE = 0.019204063816351407
Epoch: 6800 RMSE = 0.019109384519353987
Epoch: 6900 RMSE = 0.01897017115471263
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9881577021080794
Output:  0.012095711137474456
Output:  0.005415717530674342
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.009033977094723342
Output:  0.9951035364697258
Output:  0.0012599570492609427
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9932153477209283
Output:  0.01592489154203647
Output:  0.007792737035077389
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01725433186907098
Output:  0.9986800919155656
Output:  0.003194894017951176
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9857115281539325
Output:  0.006129785965112039
Output:  0.0038134823332998495
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9893066721713704
Output:  0.009540809983525612
Output:  0.005642997410570359
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0010824222965141032
Output:  0.9021023643482539
Output:  0.07882934811388904
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  2.9282747879014126e-06
Output:  0.002283227351157341
Output:  0.9895599826887449
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9898203678162381
Output:  0.010519001823720939
Output:  0.006120662179462684
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9899115910368844
Output:  0.012499767578617014
Output:  0.005865361325614256
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9857119357111197
Output:  0.006132295701713594
Output:  0.0038123901239990724
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.013933003372605432
Output:  0.9977323573312404
Output:  0.0022989307001215708
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9923954849405592
Output:  0.01318269692645335
Output:  0.007618640664677586
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.992674680325971
Output:  0.012769508075317557
Output:  0.0075472083138455074
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.0073797354169545136
Output:  0.9925513020893427
Output:  0.001076143253667209
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.01987312488722461
Output:  0.9987478155398938
Output:  0.003293204651454049
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  2.85241796155621e-06
Output:  0.0018887847419105678
Output:  0.9882380163239408
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9945583166784631
Output:  0.023642431331916142
Output:  0.013679678329521822
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9920303266183113
Output:  0.015555682226708212
Output:  0.008900031913409774
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  3.0616700322910363e-06
Output:  0.0017431942173598068
Output:  0.989273778133734
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9899294989695913
Output:  0.014284930466930969
Output:  0.008289641909347984
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  2.631664956026979e-06
Output:  0.0016353314303949333
Output:  0.9879209504489334
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9937634215692847
Output:  0.020920414852558376
Output:  0.010627953044952218
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  4.58973092220023e-06
Output:  0.006603810130373444
Output:  0.9957891040247258
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  1.6787615651379524e-06
Output:  0.0011066619100791966
Output:  0.984409314498521
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9932589352785015
Output:  0.02640480038713271
Output:  0.014939924018138562
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  4.7875152283524064e-06
Output:  0.0055141885745200285
Output:  0.9950314552485844
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  3.874792055786492e-06
Output:  0.0040965870001978865
Output:  0.9935163220997664
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  6.406015678755504e-06
Output:  0.009377619115338888
Output:  0.9965965964774317
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004903660767226853
Output:  0.9815516592725952
Output:  0.0004787562385364185
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.991929141098749
Output:  0.014125709267324482
Output:  0.008213502286894336
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  4.0867810045063086e-06
Output:  0.003248893678818871
Output:  0.9930245554037815
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9905197153445018
Output:  0.00964898780092353
Output:  0.0059831212438770775
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.009540289149659932
Output:  0.9956929173451952
Output:  0.0013192993760670329
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.005365897356726254
Output:  0.9935094913577044
Output:  0.0011387665435525199
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  8.114797424205222e-06
Output:  0.01765278171555431
Output:  0.9979386644390958
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  6.65097906504007e-06
Output:  0.01959993772433261
Output:  0.9981034096340459
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.0047862834704448425
Output:  0.988723212271678
Output:  0.001449630945397034
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  5.62320869304184e-06
Output:  0.009467050602486086
Output:  0.996796518509438
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.988290137174456
Output:  0.005979610895054516
Output:  0.004263046455871211
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  3.086460506861921e-06
Output:  0.0030815352286080035
Output:  0.9925918692117272
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9855556445193233
Output:  0.00623997592268058
Output:  0.003552217551617902
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.011215989931356368
Output:  0.9967621754738517
Output:  0.002176456583658275
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  2.85024028847164e-05
Output:  0.054156213027113424
Output:  0.869405832766499
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  6.4557823535068754e-06
Output:  0.009014147157837516
Output:  0.9965733685685627
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  6.324639811371091e-06
Output:  0.006336062078867037
Output:  0.995538610188138
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9957146514753806
Output:  0.03718783240287932
Output:  0.01909524627952807
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.989264676927017
Output:  0.010218789006030335
Output:  0.005338453191106392
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  2.8708892673218438e-06
Output:  0.0029130673052923137
Output:  0.9903381749459738
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  1.34096423614377e-05
Output:  0.01960965035030063
Output:  0.9530112872045811
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.0091390170116176
Output:  0.997376058860528
Output:  0.0041510476515702775
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  3.3602139308921687e-06
Output:  0.003742535758243203
Output:  0.9934058709823164
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.012052085909822988
Output:  0.9973026726823581
Output:  0.0018524239846685912
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  1.917286272177837e-05
Output:  0.040845805665484285
Output:  0.9693189680489903
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  5.991846449233013e-06
Output:  0.009590964971773723
Output:  0.9967970299869093
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  2.5719782095206578e-06
Output:  0.0014636371467906311
Output:  0.9868494591857787
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9837956455890807
Output:  0.005942629592782781
Output:  0.0035797780512622805
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9917139462289287
Output:  0.013062892385920682
Output:  0.00718750774817154
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  7.252740792631676e-06
Output:  0.016349632406573045
Output:  0.9977920768813769
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.012420260883637175
Output:  0.9980962398363351
Output:  0.002483173201968323
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0013615884270794863
Output:  0.9596870761810709
Output:  0.09677364269441471
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9849655805510191
Output:  0.00405508398527074
Output:  0.00275512911855038
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  4.616779175559532e-06
Output:  0.0045485366979603585
Output:  0.993998004890775
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9847826198428646
Output:  0.004963300846185881
Output:  0.003019143520268718
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9891548038674989
Output:  0.008672648894657194
Output:  0.005202995752614124
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.01589917676198709
Output:  0.9988600134877053
Output:  0.0037085838338240715
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  5.221017800754196e-06
Output:  0.008595088878678393
Output:  0.9959818631982246
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.989296131924321
Output:  0.00930967132703511
Output:  0.0056248125548787374
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.011296308606099441
Output:  0.9959233999964161
Output:  0.0013846113324647545
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.007846180525019432
Output:  0.9933879244925687
Output:  0.0021230865134780237
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  6.2281889134726815e-06
Output:  0.009896828609490206
Output:  0.9970118511995284
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.009855902395199482
Output:  0.9970480983082666
Output:  0.0017895108256557382
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.009398454877326639
Output:  0.9961929680782676
Output:  0.0027860958391040156
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9836765916613316
Output:  0.00506819682410126
Output:  0.003261100677284515
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.006071513049153927
Output:  0.9825285901180082
Output:  0.0006294689996359139
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  1.0383877235256284e-05
Output:  0.020484727552825013
Output:  0.9981952134480941
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9856113466576922
Output:  0.005396239957276955
Output:  0.0035117496633117425
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.981976269241932
Output:  0.0035870586327424524
Output:  0.0023803856722702226
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9896820856732484
Output:  0.014321817453284947
Output:  0.007370660091938546
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9880776221276024
Output:  0.0061135607523380145
Output:  0.0038010472125857763
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0030683280945519057
Output:  0.9727544531752252
Output:  0.0037602733821319833
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  8.011120415497376e-06
Output:  0.012995387767179642
Output:  0.9967808643954643
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  1.737834311551342e-05
Output:  0.03893736144078936
Output:  0.998880402093507
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.0120764806584001
Output:  0.9976811112578713
Output:  0.0021154058422874237
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9857127377501955
Output:  0.006129771416816577
Output:  0.0038118938506568538
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.011893199641163879
Output:  0.996185276048863
Output:  0.0014851856498212755
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.00908405348145304
Output:  0.994831434535838
Output:  0.0012711311873221367
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  5.821740582394566e-06
Output:  0.005408319913488775
Output:  0.9948971248321867
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9941120347002479
Output:  0.015976004244990943
Output:  0.009941660005122858
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9890690123686546
Output:  0.01022374110854734
Output:  0.006092708040250291
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  6.845042209380816e-06
Output:  0.017275749102101782
Output:  0.9975842024712452
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004502278278774023
Output:  0.9821815732676824
Output:  0.00048400657220862146
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.984654762095945
Output:  0.007091335784219132
Output:  0.0038847279967579884
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  1.3457864622259365e-05
Output:  0.02034490723361998
Output:  0.9480947467707037
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.01935277085066657
Output:  0.9991732008694639
Output:  0.0047015265326151665
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.008397372543113882
Output:  0.9953926336680472
Output:  0.0012854220360545981
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9927146491564768
Output:  0.01900795992625362
Output:  0.010459095963832092
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.008495383415039614
Output:  0.9936053298686066
Output:  0.0025755063359051166
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  4.7767628617136985e-06
Output:  0.009437606430540429
Output:  0.9958670389516788
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0019832838032592037
Output:  0.955016292301669
Output:  0.000819445640688765
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.005341654524402374
Output:  0.9853417356622794
Output:  0.00383788109090239
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  2.1228232260318637e-06
Output:  0.0013240717577783585
Output:  0.9851313600093522
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.006768460103599183
Output:  0.9931061434885903
Output:  0.0009505989491536847
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.005837273913617514
Output:  0.9909972110881129
Output:  0.000788324645467499
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9807156784136769
Output:  0.002873697727296965
Output:  0.0021607155016530274
Epoch: 7000 RMSE = 0.018943136137996166
Epoch: 7100 RMSE = 0.01879593493554609
Epoch: 7200 RMSE = 0.018636477509935884
Epoch: 7300 RMSE = 0.018611854065813463
Epoch: 7400 RMSE = 0.018367287237338548
Epoch: 7500 RMSE = 0.01840540257368002
Epoch: 7600 RMSE = 0.01843077406805693
Epoch: 7700 RMSE = 0.01830658622852579
Epoch: 7800 RMSE = 0.018282185226251108
Epoch: 7900 RMSE = 0.01826632628269925
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9849803990019795
Output:  0.005475252427101997
Output:  0.0031949765932686937
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9900661863615235
Output:  0.008589354470390567
Output:  0.005021804963856301
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9860576450017023
Output:  0.003736919002767219
Output:  0.0024595130051167386
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9891247491956268
Output:  0.005516759823105382
Output:  0.003806722404057322
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  1.5482071063562227e-06
Output:  0.0010663486026580953
Output:  0.9841280716135076
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9937256983605078
Output:  0.014667470972178883
Output:  0.006960404427396088
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  5.909200251476126e-06
Output:  0.009041734093928862
Output:  0.9965334864952133
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  3.100076244058119e-06
Output:  0.0036106504830167
Output:  0.9932672217173224
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.988947299612339
Output:  0.005634317764802148
Output:  0.003393724659747857
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  3.5748022936532884e-06
Output:  0.0039497831858735875
Output:  0.9933954528887475
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9912019361538785
Output:  0.008900488076158128
Output:  0.005344308081661078
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004537759964518063
Output:  0.9838776851833471
Output:  0.00041754938417971535
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  5.35771457728404e-06
Output:  0.005203507172965465
Output:  0.9948088512116565
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.008737227849725191
Output:  0.9978118468833657
Output:  0.003479338896546703
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.01032252856152699
Output:  0.9971550418500144
Output:  0.001913193626812278
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  5.8339469910522484e-06
Output:  0.006111413542888261
Output:  0.9954468251185823
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  1.8573118542972106e-05
Output:  0.04349827910586079
Output:  0.9660839482900415
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9945335726046846
Output:  0.014754950746010539
Output:  0.008879430850057947
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  4.225291562003683e-06
Output:  0.006347345406306372
Output:  0.995722341422467
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9906503972244101
Output:  0.013183107253822159
Output:  0.007406278815170556
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.005651905460316577
Output:  0.9846265254872856
Output:  0.000549147199359384
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  1.9585475697697497e-06
Output:  0.0012772835409983157
Output:  0.9848311462216423
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.001418196600202994
Output:  0.9686945039339484
Output:  0.07654028366071111
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  1.3273305841980552e-05
Output:  0.021545785618905938
Output:  0.9467988218166339
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9949477724785961
Output:  0.021840466001851227
Output:  0.012226549844074635
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.01289029914302099
Output:  0.998025765404913
Output:  0.002002776574255737
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.993203958468332
Output:  0.011779062268874289
Output:  0.0067382892246208035
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.010998861096652641
Output:  0.9966806904439011
Output:  0.0012937298328940991
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.014706613221415426
Output:  0.9990081144012237
Output:  0.003231884328825289
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.008410293112049426
Output:  0.9954919272430738
Output:  0.0011077084026166093
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.005399344922082209
Output:  0.9921613452815675
Output:  0.0006861120526819775
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9867545019158978
Output:  0.005648491474850906
Output:  0.003403243626979159
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  2.6041961351388508e-06
Output:  0.001796069831079003
Output:  0.988144568250562
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  4.787126630642388e-06
Output:  0.008236177375205742
Output:  0.9959202878818143
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  2.8218324682240147e-06
Output:  0.0016783863582807675
Output:  0.9890682447661862
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.011170439008203142
Output:  0.9976610361462378
Output:  0.001606141062112259
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9898557254821213
Output:  0.00943337828822067
Output:  0.005436453255630465
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  4.406906137602347e-06
Output:  0.005301511713708603
Output:  0.9949429694623136
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  2.4270228805186503e-06
Output:  0.0015758810147552074
Output:  0.987680581915227
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.008083582263133928
Output:  0.9946192123357599
Output:  0.0021720675898467155
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9932364994175054
Output:  0.01755912991382625
Output:  0.00933472540100728
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  1.5972551017466134e-05
Output:  0.037457096833696184
Output:  0.9988603305633226
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  4.238552894413982e-06
Output:  0.0043630684030446865
Output:  0.9938982410088031
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.018393116205999153
Output:  0.9989107986046978
Output:  0.0028647376069442414
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9900819675865589
Output:  0.008798731881332242
Output:  0.005033323823905352
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.017955893667038477
Output:  0.9992837905815527
Output:  0.004077743615362693
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9866341297344129
Output:  0.005740659753612987
Output:  0.0031721146839696662
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9859101641239658
Output:  0.004568593103972747
Output:  0.002694382233130911
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  5.74497096414979e-06
Output:  0.009548214672218664
Output:  0.9969463243724287
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  4.381119245814301e-06
Output:  0.00905470533077082
Output:  0.9957989065613836
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9899417574331348
Output:  0.007996119407938354
Output:  0.004642627570802322
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  6.314595487252424e-06
Output:  0.016677393956500815
Output:  0.9975309195888035
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.004955699948900931
Output:  0.9943333257973913
Output:  0.0009935778583322408
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9929443453232585
Output:  0.012160468736521305
Output:  0.0067981526793267875
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9904347915212315
Output:  0.013206620894372004
Output:  0.006578872925148614
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.990555983117119
Output:  0.009699135530903664
Output:  0.005460840833824179
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9848636388556945
Output:  0.0046697012923840155
Output:  0.002909567792120306
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.01596576265951406
Output:  0.9988528598004838
Output:  0.0027772621733364203
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  7.4857642897883835e-06
Output:  0.017023597176594775
Output:  0.9978963636399696
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.007765898552312524
Output:  0.9959902727125511
Output:  0.0011179560733313644
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9858005040679365
Output:  0.006525949531198197
Output:  0.003467641342063082
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004166144556351979
Output:  0.9844498884592772
Output:  0.000420983291439634
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.001178012620785366
Output:  0.9271308119347221
Output:  0.058963884177783386
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.994217653332914
Output:  0.01930518402299592
Output:  0.00949142555428355
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.008353651644777861
Output:  0.9957424697283895
Output:  0.0010947869386051627
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.009115224668214864
Output:  0.997432464670166
Output:  0.0015563670611392867
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9820976026800357
Output:  0.0026495500877884975
Output:  0.001926689726647762
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  2.671875942924976e-06
Output:  0.0028546435353998556
Output:  0.9899896766441949
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.00684008632261789
Output:  0.9934878461089226
Output:  0.0009364590475084959
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  5.955390572387831e-06
Output:  0.008699155873482578
Output:  0.9964946867043556
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.004499783128221515
Output:  0.9903476197262093
Output:  0.0012409408165212849
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0019362602117292
Output:  0.9631980485602926
Output:  0.0006691436575849733
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.989071869044166
Output:  0.0111199884498486
Output:  0.004834385335834888
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  2.3730739053682407e-06
Output:  0.0014132944056371014
Output:  0.9865412188776287
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  2.8461648822258777e-06
Output:  0.0029710242631502157
Output:  0.992441263175769
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  9.578685436145006e-06
Output:  0.019783855559269457
Output:  0.9981547954798671
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9926036336948858
Output:  0.01435781256022107
Output:  0.007945631505979866
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.011489769722639126
Output:  0.9983457362502623
Output:  0.002157379169425308
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  2.5933414113481723e-05
Output:  0.05360556368155018
Output:  0.8655514323973712
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  3.7654228691675955e-06
Output:  0.0031270162865979765
Output:  0.9929052198464803
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  2.701178838866139e-06
Output:  0.0022014246930807816
Output:  0.9893492498752943
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  7.24151547655609e-06
Output:  0.012216087378498205
Output:  0.9967933480001671
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0027670641871602743
Output:  0.9748595047239641
Output:  0.0034297262527713647
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.010445749730954969
Output:  0.9964532546482876
Output:  0.001206253219940794
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.004931826000723465
Output:  0.9869845484343968
Output:  0.003388548473954134
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.00867756291765202
Output:  0.9966616402123588
Output:  0.0024419137654989567
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9906761849965168
Output:  0.011497808572760523
Output:  0.005240072510404628
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  5.525997145631662e-06
Output:  0.009254158545321196
Output:  0.9967301556409021
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9832948578911127
Output:  0.00330368215885323
Output:  0.0021251983240607782
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9960219341665235
Output:  0.03439943516337368
Output:  0.017065413673584173
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9866520474993473
Output:  0.004974479330594287
Output:  0.0031348652735661087
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  6.1349242414180434e-06
Output:  0.018905295201642646
Output:  0.9980681720647288
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9937402797288268
Output:  0.02440060713228817
Output:  0.01335485651736261
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.990064359013896
Output:  0.009408811717609423
Output:  0.004767029395172441
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  5.185677772905679e-06
Output:  0.009124744295201312
Output:  0.9967380216430177
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.006261117568462436
Output:  0.9940035873743229
Output:  0.0008272710794979887
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.986755244939179
Output:  0.005648307644053175
Output:  0.003403354631423869
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  1.112070647796823e-05
Output:  0.017278572979233246
Output:  0.952821305573114
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9925102622609934
Output:  0.013033514743405432
Output:  0.007338541902046924
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9923161810144672
Output:  0.012049361166066185
Output:  0.006416387253252604
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.98675545407509
Output:  0.0056481203578769255
Output:  0.0034036990715159343
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.007208533130217354
Output:  0.9941507912099962
Output:  0.0018740720563123307
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.008814192947896071
Output:  0.9962458615389632
Output:  0.0011518202199885994
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.011167100151646068
Output:  0.9979830455629031
Output:  0.0018434551338677124
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  6.690560573162218e-06
Output:  0.01578084358620151
Output:  0.997745874216534
Epoch: 8000 RMSE = 0.018109904664380654
Epoch: 8100 RMSE = 0.01805595107576924
Epoch: 8200 RMSE = 0.017924221267615625
Epoch: 8300 RMSE = 0.018008994757791028
Epoch: 8400 RMSE = 0.017909862364997524
Epoch: 8500 RMSE = 0.017876250815155762
Epoch: 8600 RMSE = 0.01775985335967719
Epoch: 8700 RMSE = 0.017726337507433375
Epoch: 8800 RMSE = 0.01769337258502672
Epoch: 8900 RMSE = 0.017628092485847704
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9929809987541394
Output:  0.012193011933535905
Output:  0.0066269067374679
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.009764216888920959
Output:  0.9968716954103554
Output:  0.0010563854400341332
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  5.721184379331464e-06
Output:  0.018516823227892408
Output:  0.9979787741910684
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.008321804003600837
Output:  0.9981151522036
Output:  0.0029824396295928743
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  4.439077529988909e-06
Output:  0.008008882526894665
Output:  0.9957667888267329
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9907106845111803
Output:  0.008224432137357036
Output:  0.004547924885011767
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.00825228457110465
Output:  0.9966980780189099
Output:  0.0010061946297948575
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9930683526554844
Output:  0.01342982079136093
Output:  0.0071816534721295235
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  2.6529013756044097e-06
Output:  0.0029055200025383233
Output:  0.9921151040478434
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.0046496118257718586
Output:  0.9950275727727376
Output:  0.0008670795750577122
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.01721355869760114
Output:  0.999041235320122
Output:  0.002509644938271879
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  5.553141625022852e-06
Output:  0.008514321915722853
Output:  0.9963410681424432
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9875995645310305
Output:  0.005276116595614569
Output:  0.003073166124713855
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  2.4488045703617746e-06
Output:  0.0027294204183282173
Output:  0.9897682337502696
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  5.357011394662097e-06
Output:  0.009349659229203925
Output:  0.9968112734689303
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  3.5108579296351814e-06
Output:  0.0030609131593228455
Output:  0.9925800918154187
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.006995072452168823
Output:  0.9950932405937319
Output:  0.0015680932296867865
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.0076732766934715
Output:  0.9953321926075873
Output:  0.0018739050728935464
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.01073651667880614
Output:  0.998540276679873
Output:  0.00189328511374885
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  2.417754422665299e-06
Output:  0.0017492418516953099
Output:  0.9876642629945072
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.993632893675403
Output:  0.011016682728970772
Output:  0.006081937595107267
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.985825922857154
Output:  0.004362484732565546
Output:  0.0026271487582156306
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.993660310732881
Output:  0.016433805916296975
Output:  0.008431605457904548
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  8.925200872384176e-06
Output:  0.019350773667584767
Output:  0.9980720175859897
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.005317465164194767
Output:  0.9862977005015405
Output:  0.00048119860414522816
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0011312577717950694
Output:  0.9349832881859462
Output:  0.05156492839238256
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.0038972761261526845
Output:  0.9862586603611042
Output:  0.0003685805226191315
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.005146653971896393
Output:  0.9900985927439542
Output:  0.002591214203494659
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9917549381294405
Output:  0.008324553623488587
Output:  0.004821921909287796
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9843631920371322
Output:  0.0030850820438022824
Output:  0.0019174683984639932
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.009822692172419026
Output:  0.99755462943349
Output:  0.0016362397171985432
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9907103451440761
Output:  0.008785955875794785
Output:  0.004302799865157187
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  4.996891093919525e-06
Output:  0.005101435185380758
Output:  0.9945556028242626
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  2.630786531442051e-06
Output:  0.0016437291400138397
Output:  0.98856703318303
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9912352774167861
Output:  0.01233740743655223
Output:  0.006683033159261023
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.007869726816089797
Output:  0.996016305783338
Output:  0.0009695613251150609
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9859409749148655
Output:  0.005114012816216169
Output:  0.0028828598983681726
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  3.940383183268737e-06
Output:  0.006222023680549027
Output:  0.9955141463571725
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9867282603464934
Output:  0.006090871907925567
Output:  0.003131778147513901
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9868239883701849
Output:  0.004264781890788613
Output:  0.002432991227989367
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9952638262270407
Output:  0.02045467568577197
Output:  0.011038633830900979
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9898027729189378
Output:  0.0051601141722767046
Output:  0.0034338760267347006
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9904949371754331
Output:  0.00882181066695894
Output:  0.004908458229596352
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9928038914856235
Output:  0.011268281385949003
Output:  0.005790077763625621
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  5.439818545975482e-06
Output:  0.005986787191786939
Output:  0.9952273043533088
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9898093126143244
Output:  0.010362704563922215
Output:  0.004368953494946565
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9911528586034168
Output:  0.009070505437724356
Output:  0.004930618558565138
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0029346995426289863
Output:  0.9811976319202094
Output:  0.002574182557297564
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  1.4900427573073374e-05
Output:  0.036764686455261146
Output:  0.9988061519163788
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9874963562257666
Output:  0.0046489196251787235
Output:  0.002828257848446614
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.010442734527144788
Output:  0.9982236698586885
Output:  0.0016109472933900834
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.994585818725493
Output:  0.018056434109105627
Output:  0.008575028266411462
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  1.1741957095805196e-05
Output:  0.020760155511524592
Output:  0.9418008117326998
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.008450130082153501
Output:  0.997217878285433
Output:  0.0020313146059138913
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  1.4435279601696897e-06
Output:  0.001044140328508992
Output:  0.9833811803593122
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  2.8907316149843817e-06
Output:  0.0035360934997610695
Output:  0.9929466433550762
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  1.2447739162478391e-05
Output:  0.02182710747351968
Output:  0.9432254386241026
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.010278498087974002
Output:  0.9970730254184907
Output:  0.0011325488348579897
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9941379116546903
Output:  0.01369281204470734
Output:  0.0062860479747079
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9905806929380998
Output:  0.0074738699425008145
Output:  0.004193100193781787
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.996271345761138
Output:  0.032234422484074134
Output:  0.015418901574569361
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  4.106375627928868e-06
Output:  0.005186495384256075
Output:  0.9947179156630801
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9941310436898897
Output:  0.022852956092237628
Output:  0.012061716691687416
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.013745998752901372
Output:  0.9991253760809764
Output:  0.0028302501951285785
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9876004149077435
Output:  0.005276116181483403
Output:  0.0030718415636378227
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.006409910255775121
Output:  0.9942280537286828
Output:  0.0008216327453139568
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9869438163951956
Output:  0.003490392240994822
Output:  0.0022195434050959017
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9948761391319443
Output:  0.01380812616969825
Output:  0.008015502715121005
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  5.888772532546018e-06
Output:  0.016338564195124635
Output:  0.997418363444525
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  3.940699491703612e-06
Output:  0.004258524889362133
Output:  0.993641828691978
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0015152515366904156
Output:  0.9762459057985053
Output:  0.05879799447142877
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  3.333359648897708e-06
Output:  0.003867707641489891
Output:  0.9930812313525486
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  6.239411226779398e-06
Output:  0.015460294044890556
Output:  0.9976373235190393
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  6.824953130247292e-06
Output:  0.012178106372214557
Output:  0.9965895677220274
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9933899431174357
Output:  0.011373356892731949
Output:  0.006139478482081838
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9875083886969616
Output:  0.005356047319870182
Output:  0.0028651186823863838
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.008519138042009565
Output:  0.9977342862254783
Output:  0.0013641606698717964
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.00423481476382866
Output:  0.9915222747709386
Output:  0.0010808535245972009
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.004244860373973112
Output:  0.9857338152026582
Output:  0.0003653568443190323
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.010453954343523338
Output:  0.9979418999176324
Output:  0.001404540119036779
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  2.5190185298576744e-06
Output:  0.0021556669668195893
Output:  0.9888440411995313
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  2.264952599977566e-05
Output:  0.04965474457003045
Output:  0.8675849529208692
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9832211043360326
Output:  0.0024752078818027863
Output:  0.0017409175184006937
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  6.980970994027754e-06
Output:  0.01667310177148493
Output:  0.9978042992250648
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.991294036879024
Output:  0.01072324808324137
Output:  0.00473512150834348
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  2.2627053726924905e-06
Output:  0.0015418613390455963
Output:  0.9871512118201284
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.014922782035244619
Output:  0.9989884717550255
Output:  0.002437615730625871
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.007804662343445595
Output:  0.996240845482612
Output:  0.0009611823370353444
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  4.835217420099438e-06
Output:  0.008932399011755732
Output:  0.9965899163632024
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.005045402679996246
Output:  0.9930782167515503
Output:  0.0006013556004644252
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0017288184686504579
Output:  0.9649220706450989
Output:  0.000625712721148225
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.012040985127587712
Output:  0.9982572399784017
Output:  0.0017570239242532446
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9876004943860545
Output:  0.005275663666234378
Output:  0.003073718189544531
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  2.211037444881896e-06
Output:  0.0013812368167545569
Output:  0.9859796020246877
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9910456878043865
Output:  0.01234346832999762
Output:  0.005946904143495326
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  5.151617163978115e-06
Output:  0.009056214157919476
Output:  0.9965825462531548
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9896527521631018
Output:  0.005262420725226679
Output:  0.0030647955823214514
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.016779332069696336
Output:  0.999368090342416
Output:  0.0035816556799077998
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9906918402448066
Output:  0.008029616205613798
Output:  0.004535061856781208
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  1.5669509691220272e-05
Output:  0.03790103155304727
Output:  0.9682758137010797
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  5.509335446736619e-06
Output:  0.008848944299186777
Output:  0.996376809544966
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.005853665474877759
Output:  0.9947125362715324
Output:  0.0007244153693023637
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.007256640045882295
Output:  0.9964612289069656
Output:  0.0009812284901043404
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  4.013858422614697e-06
Output:  0.008654517955376334
Output:  0.9957096869247964
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  1.826169848274664e-06
Output:  0.0012502967197134337
Output:  0.9841496849426095
Epoch: 9000 RMSE = 0.01754266490660893
Epoch: 9100 RMSE = 0.01758952690507126
Epoch: 9200 RMSE = 0.017453089950699482
Epoch: 9300 RMSE = 0.017495672089830275
Epoch: 9400 RMSE = 0.017441491898321955
Epoch: 9500 RMSE = 0.017331141442828664
Epoch: 9600 RMSE = 0.01737495011970582
Epoch: 9700 RMSE = 0.01730816655370755
Epoch: 9800 RMSE = 0.01726489909654251
Epoch: 9900 RMSE = 0.017260069624195202
Feature: [5.  3.  1.6 0.2], Label: [1. 0. 0.]
Output:  0.9875003087532276
Output:  0.005748832246650989
Output:  0.0028639600663480725
Feature: [6.4 3.2 5.3 2.3], Label: [0. 0. 1.]
Output:  3.855878578375623e-06
Output:  0.00513880832346438
Output:  0.9944239786289059
Feature: [4.6 3.4 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9902389574256446
Output:  0.004974437705180371
Output:  0.002799361705221734
Feature: [6.1 2.8 4.7 1.2], Label: [0. 1. 0.]
Output:  0.009193281222767793
Output:  0.9978051245454306
Output:  0.0014648153577697738
Feature: [5.9 3.2 4.8 1.8], Label: [0. 1. 0.]
Output:  0.0010274070764279826
Output:  0.9366245281810384
Output:  0.048986523101862925
Feature: [5.8 2.8 5.1 2.4], Label: [0. 0. 1.]
Output:  2.3686087923241915e-06
Output:  0.0021408524244675977
Output:  0.9882086116315479
Feature: [6.8 3.2 5.9 2.3], Label: [0. 0. 1.]
Output:  5.221528538642035e-06
Output:  0.008457305404645437
Output:  0.9961253518780631
Feature: [4.6 3.1 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9875839152791415
Output:  0.004027121040194861
Output:  0.0022243722577518763
Feature: [6.  2.9 4.5 1.5], Label: [0. 1. 0.]
Output:  0.008007387004303854
Output:  0.9975455090426659
Output:  0.0017900743913269578
Feature: [5.  3.5 1.6 0.6], Label: [1. 0. 0.]
Output:  0.9918062042605531
Output:  0.01012523161690911
Output:  0.004326804430699176
Feature: [4.8 3.  1.4 0.1], Label: [1. 0. 0.]
Output:  0.9866283524172279
Output:  0.004123383058271846
Output:  0.002401176670574568
Feature: [5.8 2.7 5.1 1.9], Label: [0. 0. 1.]
Output:  2.127573788970733e-06
Output:  0.0015318051686581664
Output:  0.9863927263949464
Feature: [6.4 2.8 5.6 2.2], Label: [0. 0. 1.]
Output:  3.1343282352571328e-06
Output:  0.0038409475782469286
Output:  0.9926857752968801
Feature: [5.7 2.8 4.5 1.3], Label: [0. 1. 0.]
Output:  0.006718006587256039
Output:  0.9957539362469793
Output:  0.0013568482382919128
Feature: [5.1 3.8 1.5 0.3], Label: [1. 0. 0.]
Output:  0.9937603881364574
Output:  0.010762514989345872
Output:  0.005612263927096186
Feature: [6.1 2.6 5.6 1.4], Label: [0. 0. 1.]
Output:  2.472406014894715e-06
Output:  0.0016303521240557176
Output:  0.9879314798111121
Feature: [6.  2.2 4.  1. ], Label: [0. 1. 0.]
Output:  0.004399819260726063
Output:  0.995616249375571
Output:  0.0007634132248403086
Feature: [5.  3.6 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9922162089535042
Output:  0.007874448932583357
Output:  0.004407896909588531
Feature: [6.7 3.  5.  1.7], Label: [0. 1. 0.]
Output:  0.0014509843981142126
Output:  0.9786913145659372
Output:  0.05222400427777909
Feature: [4.8 3.1 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9882341850248673
Output:  0.005057698484273058
Output:  0.002619085855446695
Feature: [6.  3.  4.8 1.8], Label: [0. 0. 1.]
Output:  2.0763056219368215e-05
Output:  0.049038194004584666
Output:  0.8630106128070267
Feature: [6.  2.2 5.  1.5], Label: [0. 0. 1.]
Output:  1.356945565016077e-06
Output:  0.0010360432271244386
Output:  0.982482597636809
Feature: [7.7 3.8 6.7 2.2], Label: [0. 0. 1.]
Output:  1.386007235672286e-05
Output:  0.035953361936347086
Output:  0.9987577891235293
Feature: [4.9 3.  1.4 0.2], Label: [1. 0. 0.]
Output:  0.9867413281837338
Output:  0.00483109686955953
Output:  0.0026373103453873636
Feature: [6.  2.7 5.1 1.6], Label: [0. 1. 0.]
Output:  2.253864739497938e-06
Output:  0.0017158385757986524
Output:  0.9871076621304965
Feature: [6.3 2.7 4.9 1.8], Label: [0. 0. 1.]
Output:  2.2668037713306942e-06
Output:  0.0026522562151613557
Output:  0.9893777319409179
Feature: [5.7 2.6 3.5 1. ], Label: [0. 1. 0.]
Output:  0.006058233671381876
Output:  0.9948537538410432
Output:  0.0007290067966937342
Feature: [6.1 2.8 4.  1.3], Label: [0. 1. 0.]
Output:  0.008025742034217635
Output:  0.9979888079073783
Output:  0.0012099991456152534
Feature: [5.6 2.9 3.6 1.3], Label: [0. 1. 0.]
Output:  0.007426143583531629
Output:  0.9964551121526123
Output:  0.0008604765475676758
Feature: [6.9 3.2 5.7 2.3], Label: [0. 0. 1.]
Output:  4.842945107591206e-06
Output:  0.008991760968688116
Output:  0.9963802841536611
Feature: [5.6 2.8 4.9 2. ], Label: [0. 0. 1.]
Output:  2.0784771917064382e-06
Output:  0.001371231420809948
Output:  0.9851602939612255
Feature: [5.7 3.  4.2 1.2], Label: [0. 1. 0.]
Output:  0.009682590533105407
Output:  0.9974021673047728
Output:  0.0010041079188672873
Feature: [7.7 2.6 6.9 2.3], Label: [0. 0. 1.]
Output:  5.5371273855263035e-06
Output:  0.016223953978353054
Output:  0.9972695931504979
Feature: [5.4 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.004484330534897396
Output:  0.9900173262612895
Output:  0.002557573324203681
Feature: [6.5 3.  5.5 1.8], Label: [0. 0. 1.]
Output:  3.6691271154417035e-06
Output:  0.004170416667179007
Output:  0.9933587060759592
Feature: [5.5 3.5 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9917230763014059
Output:  0.011674401217206634
Output:  0.006110396218971835
Feature: [5.5 2.5 4.  1.3], Label: [0. 1. 0.]
Output:  0.0038618091999950317
Output:  0.9920658327881845
Output:  0.0010018267161976116
Feature: [6.7 3.3 5.7 2.5], Label: [0. 0. 1.]
Output:  5.18035555537418e-06
Output:  0.008789902020938779
Output:  0.9961610635014528
Feature: [5.3 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9933736732597631
Output:  0.01153826875427302
Output:  0.0060548940684723804
Feature: [5.1 2.5 3.  1.1], Label: [0. 1. 0.]
Output:  0.005047139994771539
Output:  0.9877109823498944
Output:  0.00042750454748038
Feature: [5.1 3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9912344830776332
Output:  0.00777790487526934
Output:  0.004155013999416954
Feature: [6.1 3.  4.9 1.8], Label: [0. 0. 1.]
Output:  9.797033280885644e-06
Output:  0.017058144085612577
Output:  0.9513936956063253
Feature: [5.4 3.9 1.7 0.4], Label: [1. 0. 0.]
Output:  0.9948919149681211
Output:  0.01708255702554429
Output:  0.007843544317946628
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9883040315368865
Output:  0.00498660468444266
Output:  0.002807885256174972
Feature: [5.  3.4 1.6 0.4], Label: [1. 0. 0.]
Output:  0.9912484862319315
Output:  0.008296942536351345
Output:  0.003935322114217636
Feature: [4.4 3.  1.3 0.2], Label: [1. 0. 0.]
Output:  0.9852542091831777
Output:  0.0029138881621072056
Output:  0.0017531591773745586
Feature: [7.7 2.8 6.7 2. ], Label: [0. 0. 1.]
Output:  5.866974521115938e-06
Output:  0.015349962992681071
Output:  0.9975028283787103
Feature: [6.9 3.1 5.4 2.1], Label: [0. 0. 1.]
Output:  4.122481740699808e-06
Output:  0.007815799503429068
Output:  0.9955885285765552
Feature: [4.3 3.  1.1 0.1], Label: [1. 0. 0.]
Output:  0.9841568309660581
Output:  0.002340606898265544
Output:  0.0015899837427813068
Feature: [5.8 4.  1.2 0.2], Label: [1. 0. 0.]
Output:  0.9944567418487981
Output:  0.021646199500321775
Output:  0.01103063841801397
Feature: [4.9 2.4 3.3 1. ], Label: [0. 1. 0.]
Output:  0.0040036164056740505
Output:  0.9872947485355493
Output:  0.00032420902225963413
Feature: [7.6 3.  6.6 2.1], Label: [0. 0. 1.]
Output:  6.564324078279281e-06
Output:  0.01655924221252748
Output:  0.997674401912472
Feature: [6.5 2.8 4.6 1.5], Label: [0. 1. 0.]
Output:  0.007675551479470873
Output:  0.9982672728286353
Output:  0.0027217429575900265
Feature: [6.1 3.  4.6 1.4], Label: [0. 1. 0.]
Output:  0.01136568148559075
Output:  0.9984579783095386
Output:  0.0015524832522846423
Feature: [6.9 3.1 4.9 1.5], Label: [0. 1. 0.]
Output:  0.015826466685552446
Output:  0.999440340245052
Output:  0.0031688382906792044
Feature: [5.  3.4 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9911122124018756
Output:  0.007066297697792185
Output:  0.003832750646538276
Feature: [7.3 2.9 6.3 1.8], Label: [0. 0. 1.]
Output:  5.036641219118969e-06
Output:  0.009282171525524427
Output:  0.9966252450884081
Feature: [5.2 4.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9951613317405207
Output:  0.013070871506558626
Output:  0.00732794729676044
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9883042506108767
Output:  0.004986284362219646
Output:  0.0028078586619450104
Feature: [5.9 3.  4.2 1.5], Label: [0. 1. 0.]
Output:  0.009839456264404306
Output:  0.9981716114070747
Output:  0.001247174964436179
Feature: [6.9 3.1 5.1 2.3], Label: [0. 0. 1.]
Output:  3.7510572792663174e-06
Output:  0.008529448058059169
Output:  0.9954885085906944
Feature: [5.4 3.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9915536119261602
Output:  0.011672589236378724
Output:  0.0054336529330272125
Feature: [6.8 3.  5.5 2.1], Label: [0. 0. 1.]
Output:  3.697987306087832e-06
Output:  0.00615664102393834
Output:  0.9952734530278304
Feature: [5.6 2.5 3.9 1.1], Label: [0. 1. 0.]
Output:  0.0055184989355937806
Output:  0.9953129885978789
Output:  0.000640753509641278
Feature: [6.3 3.3 4.7 1.6], Label: [0. 1. 0.]
Output:  0.01621341921040234
Output:  0.9991491530942558
Output:  0.002224941795453988
Feature: [5.1 3.5 1.4 0.3], Label: [1. 0. 0.]
Output:  0.9916495795973362
Output:  0.008577410874047366
Output:  0.004508355970530226
Feature: [6.7 2.5 5.8 1.8], Label: [0. 0. 1.]
Output:  2.717998523285767e-06
Output:  0.0035095040918090657
Output:  0.9925476126044407
Feature: [5.5 4.2 1.4 0.2], Label: [1. 0. 0.]
Output:  0.995527230883947
Output:  0.019365878462437244
Output:  0.010097136746066795
Feature: [5.1 3.8 1.6 0.2], Label: [1. 0. 0.]
Output:  0.9939907206875658
Output:  0.010421154249625227
Output:  0.005560696855176323
Feature: [5.1 3.8 1.9 0.4], Label: [1. 0. 0.]
Output:  0.9944803332979427
Output:  0.012931548658512315
Output:  0.0057486089708831825
Feature: [4.9 3.1 1.5 0.1], Label: [1. 0. 0.]
Output:  0.9883042634753337
Output:  0.004986033220541108
Output:  0.002807841563631728
Feature: [5.5 2.6 4.4 1.2], Label: [0. 1. 0.]
Output:  0.0024651039112679922
Output:  0.9799483849419276
Output:  0.002667522506140642
Feature: [6.2 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.009833837637036782
Output:  0.9984229047535582
Output:  0.0014299306246962791
Feature: [7.2 3.6 6.1 2.5], Label: [0. 0. 1.]
Output:  8.386306740313531e-06
Output:  0.019191400012569106
Output:  0.9979645784902507
Feature: [6.3 2.8 5.1 1.5], Label: [0. 0. 1.]
Output:  8.785417479122073e-06
Output:  0.015053052760583748
Output:  0.9532132570399038
Feature: [6.7 3.1 4.4 1.4], Label: [0. 1. 0.]
Output:  0.012951425542907902
Output:  0.9992237830657886
Output:  0.0025109165851538795
Feature: [5.  2.  3.5 1. ], Label: [0. 1. 0.]
Output:  0.0016283051485170771
Output:  0.9685235975595274
Output:  0.0005562813949508693
Feature: [5.8 2.7 4.1 1. ], Label: [0. 1. 0.]
Output:  0.007352244660450788
Output:  0.996663899667665
Output:  0.0008514215605683057
Feature: [5.1 3.3 1.7 0.5], Label: [1. 0. 0.]
Output:  0.9904216676433518
Output:  0.009769985921972674
Output:  0.0039977670998560715
Feature: [5.5 2.4 3.7 1. ], Label: [0. 1. 0.]
Output:  0.004754357398508522
Output:  0.9938542133630703
Output:  0.0005325743076305581
Feature: [5.8 2.7 3.9 1.2], Label: [0. 1. 0.]
Output:  0.0068374500882722915
Output:  0.996859519118039
Output:  0.0008690255488969151
Feature: [6.2 3.4 5.4 2.3], Label: [0. 0. 1.]
Output:  4.674460302631201e-06
Output:  0.005025080903342701
Output:  0.9942883871816356
Feature: [5.  2.3 3.3 1. ], Label: [0. 1. 0.]
Output:  0.003674081709141655
Output:  0.9877605129934187
Output:  0.0003272667127966242
Feature: [4.4 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9876811085143571
Output:  0.003298892972766459
Output:  0.0020287740937049424
Feature: [6.4 2.9 4.3 1.3], Label: [0. 1. 0.]
Output:  0.010113552429873803
Output:  0.9987049116312301
Output:  0.0016780937973122532
Feature: [4.6 3.6 1.  0.2], Label: [1. 0. 0.]
Output:  0.9903679844187498
Output:  0.004881051130371291
Output:  0.0031393203537186123
Feature: [6.3 3.4 5.6 2.4], Label: [0. 0. 1.]
Output:  5.111830140400017e-06
Output:  0.00593591171683363
Output:  0.9949640867908762
Feature: [5.7 2.8 4.1 1.3], Label: [0. 1. 0.]
Output:  0.007769596309704371
Output:  0.9970686086015067
Output:  0.0008920787181866478
Feature: [5.1 3.7 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9932100498732311
Output:  0.010655163556670115
Output:  0.005295299248294024
Feature: [5.6 3.  4.1 1.3], Label: [0. 1. 0.]
Output:  0.009197276478178404
Output:  0.9972236922280716
Output:  0.0009362288680110323
Feature: [7.1 3.  5.9 2.1], Label: [0. 0. 1.]
Output:  4.545786751276012e-06
Output:  0.0088693487128482
Output:  0.9963899396824293
Feature: [5.4 3.9 1.3 0.4], Label: [1. 0. 0.]
Output:  0.9940138101582564
Output:  0.015555707412215111
Output:  0.007710758820657376
Feature: [7.2 3.2 6.  1.8], Label: [0. 0. 1.]
Output:  6.217769617961951e-06
Output:  0.011562386945731116
Output:  0.9965371351505607
Feature: [5.6 3.  4.5 1.5], Label: [0. 1. 0.]
Output:  0.007055233092671991
Output:  0.9956824648513686
Output:  0.001718212703958049
Feature: [6.4 2.7 5.3 1.9], Label: [0. 0. 1.]
Output:  2.493213866631044e-06
Output:  0.0028828456593280993
Output:  0.991663533345863
Feature: [5.4 3.7 1.5 0.2], Label: [1. 0. 0.]
Output:  0.9934560057835158
Output:  0.012708684213983542
Output:  0.006563314158418309
Feature: [5.2 3.4 1.4 0.2], Label: [1. 0. 0.]
Output:  0.9910272180690978
Output:  0.008342545946147528
Output:  0.004488403732391258
Feature: [6.3 2.9 5.6 1.8], Label: [0. 0. 1.]
Output:  3.298684513476701e-06
Output:  0.0030358413179485057
Output:  0.9921575826325524
Feature: [7.7 3.  6.1 2.3], Label: [0. 0. 1.]
Output:  5.37895069801609e-06
Output:  0.018383255624371576
Output:  0.9978612545374518
Feature: [5.7 4.4 1.5 0.4], Label: [1. 0. 0.]
Output:  0.9964790381923895
Output:  0.030540283968504448
Output:  0.014106306986066056
Feature: [5.7 2.5 5.  2. ], Label: [0. 0. 1.]
Output:  1.7171002309292587e-06
Output:  0.0012415564367276514
Output:  0.9832275858641737
Feature: [6.4 3.2 4.5 1.5], Label: [0. 1. 0.]
Output:  0.014060147269254027
Output:  0.9991029227733337
Output:  0.002159366878408607
Feature: [6.5 3.2 5.1 2. ], Label: [0. 0. 1.]
Output:  1.3868460903627813e-05
Output:  0.03520167318443142
Output:  0.9686025604911354
Feature: [5.  3.5 1.3 0.3], Label: [1. 0. 0.]
Output:  0.9912123827294161
Output:  0.007594895826823349
Output:  0.004143222232593019
Feature: [4.7 3.2 1.3 0.2], Label: [1. 0. 0.]
Output:  0.9881993538779896
Output:  0.0043937058129244755
Output:  0.0025860910373337624
Epoch: 10000 RMSE = 0.01707839098169245
Training finished.
 Final Training RMSE = 0.01707839098169245 

----- starting test
input_value: 4.9
input_value: 2.5
input_value: 4.5
input_value: 1.7
output_value: 1.2389956765895448e-06
expected_value: 0.0
output_value: 0.0004371381465315544
expected_value: 0.0
output_value: 0.9661279521683106
expected_value: 1.0
input_value: 5.0
input_value: 3.3
input_value: 1.4
input_value: 0.2
output_value: 0.9899679600812481
expected_value: 1.0
output_value: 0.006434848476859393
expected_value: 0.0
output_value: 0.0035543477957217665
expected_value: 0.0
input_value: 7.2
input_value: 3.0
input_value: 5.8
input_value: 1.6
output_value: 6.7670203274468526e-06
expected_value: 0.0
output_value: 0.014513542374145426
expected_value: 0.0
output_value: 0.9935036472715101
expected_value: 1.0
input_value: 6.8
input_value: 2.8
input_value: 4.8
input_value: 1.4
output_value: 0.009856384673680552
expected_value: 0.0
output_value: 0.9989331345980169
expected_value: 1.0
output_value: 0.002899226877676215
expected_value: 0.0
input_value: 4.4
input_value: 2.9
input_value: 1.4
input_value: 0.2
output_value: 0.9840774216130088
expected_value: 1.0
output_value: 0.0028715476308218244
expected_value: 0.0
output_value: 0.0016285630430121448
expected_value: 0.0
input_value: 7.0
input_value: 3.2
input_value: 4.7
input_value: 1.4
output_value: 0.016392499842323625
expected_value: 0.0
output_value: 0.9994980039570168
expected_value: 1.0
output_value: 0.0034820096627688982
expected_value: 0.0
input_value: 6.6
input_value: 3.0
input_value: 4.4
input_value: 1.4
output_value: 0.01173069600478756
expected_value: 0.0
output_value: 0.9990831229782867
expected_value: 1.0
output_value: 0.0021581607225697164
expected_value: 0.0
input_value: 4.6
input_value: 3.2
input_value: 1.4
input_value: 0.2
output_value: 0.9884011251458877
expected_value: 1.0
output_value: 0.004117640077327351
expected_value: 0.0
output_value: 0.0023914623400971284
expected_value: 0.0
input_value: 6.3
input_value: 3.3
input_value: 6.0
input_value: 2.5
output_value: 5.647215830742886e-06
expected_value: 0.0
output_value: 0.006288305821733179
expected_value: 0.0
output_value: 0.994791307778177
expected_value: 1.0
input_value: 4.8
input_value: 3.0
input_value: 1.4
input_value: 0.3
output_value: 0.9863712328469283
expected_value: 1.0
output_value: 0.004707012297628115
expected_value: 0.0
output_value: 0.0024576516121329155
expected_value: 0.0
input_value: 5.2
input_value: 3.5
input_value: 1.5
input_value: 0.2
output_value: 0.9920602399252917
expected_value: 1.0
output_value: 0.009148036047662882
expected_value: 0.0
output_value: 0.00484175797541064
expected_value: 0.0
input_value: 6.7
input_value: 3.3
input_value: 5.7
input_value: 2.1
output_value: 5.199528427944914e-06
expected_value: 0.0
output_value: 0.007389509815414808
expected_value: 0.0
output_value: 0.9958011694236282
expected_value: 1.0
input_value: 6.7
input_value: 3.1
input_value: 4.7
input_value: 1.5
output_value: 0.01443827053581931
expected_value: 0.0
output_value: 0.9993054536042075
expected_value: 1.0
output_value: 0.0026166838847286058
expected_value: 0.0
input_value: 4.8
input_value: 3.4
input_value: 1.9
input_value: 0.2
output_value: 0.9915688887107543
expected_value: 1.0
output_value: 0.006878256585406021
expected_value: 0.0
output_value: 0.00326935423513931
expected_value: 0.0
input_value: 6.7
input_value: 3.0
input_value: 5.2
input_value: 2.3
output_value: 3.234150390218883e-06
expected_value: 0.0
output_value: 0.005841541413908668
expected_value: 0.0
output_value: 0.9949496642976082
expected_value: 1.0
input_value: 7.9
input_value: 3.8
input_value: 6.4
input_value: 2.0
output_value: 0.0006669253577284619
expected_value: 0.0
output_value: 0.9383842212850707
expected_value: 0.0
output_value: 0.834778773386555
expected_value: 1.0
input_value: 5.8
input_value: 2.7
input_value: 5.1
input_value: 1.9
output_value: 2.1271003429112445e-06
expected_value: 0.0
output_value: 0.001530315620583526
expected_value: 0.0
output_value: 0.9864087414117816
expected_value: 1.0
input_value: 5.5
input_value: 2.3
input_value: 4.0
input_value: 1.3
output_value: 0.000255825796652323
expected_value: 0.0
output_value: 0.7048115059581526
expected_value: 1.0
output_value: 0.023284011897236844
expected_value: 0.0
input_value: 5.0
input_value: 3.2
input_value: 1.2
input_value: 0.2
output_value: 0.9882410406697998
expected_value: 1.0
output_value: 0.005716423073963086
expected_value: 0.0
output_value: 0.003282884331501421
expected_value: 0.0
input_value: 5.2
input_value: 2.7
input_value: 3.9
input_value: 1.4
output_value: 0.005352472002313813
expected_value: 0.0
output_value: 0.993681161947246
expected_value: 1.0
output_value: 0.0006748887574467706
expected_value: 0.0
input_value: 6.4
input_value: 3.1
input_value: 5.5
input_value: 1.8
output_value: 4.153889077331017e-06
expected_value: 0.0
output_value: 0.004397311169368229
expected_value: 0.0
output_value: 0.9928161446561551
expected_value: 1.0
input_value: 5.1
input_value: 3.5
input_value: 1.4
input_value: 0.2
output_value: 0.9916437320036535
expected_value: 1.0
output_value: 0.008102336337701433
expected_value: 0.0
output_value: 0.00444889820747939
expected_value: 0.0
input_value: 7.4
input_value: 2.8
input_value: 6.1
input_value: 1.9
output_value: 4.321335593610766e-06
expected_value: 0.0
output_value: 0.009663733052685091
expected_value: 0.0
output_value: 0.9966721183432177
expected_value: 1.0
input_value: 4.5
input_value: 2.3
input_value: 1.3
input_value: 0.3
output_value: 0.9683213238346122
expected_value: 1.0
output_value: 0.002539054050810884
expected_value: 0.0
output_value: 0.001122419307411571
expected_value: 0.0
input_value: 6.3
input_value: 2.3
input_value: 4.4
input_value: 1.3
output_value: 0.00019033460650064215
expected_value: 0.0
output_value: 0.7115987342836542
expected_value: 1.0
output_value: 0.08783010402550553
expected_value: 0.0
input_value: 6.3
input_value: 2.5
input_value: 5.0
input_value: 1.9
output_value: 1.8330779069276266e-06
expected_value: 0.0
output_value: 0.0021333413625065512
expected_value: 0.0
output_value: 0.989440309656787
expected_value: 1.0
input_value: 6.3
input_value: 2.5
input_value: 4.9
input_value: 1.5
output_value: 2.1565321047086595e-06
expected_value: 0.0
output_value: 0.002377497711360193
expected_value: 1.0
output_value: 0.9849506535587478
expected_value: 0.0
input_value: 5.7
input_value: 3.8
input_value: 1.7
input_value: 0.3
output_value: 0.994655281865318
expected_value: 1.0
output_value: 0.020105650936630335
expected_value: 0.0
output_value: 0.009172521752068997
expected_value: 0.0
input_value: 5.5
input_value: 2.4
input_value: 3.8
input_value: 1.1
output_value: 0.0047438568361361285
expected_value: 0.0
output_value: 0.9941943534362367
expected_value: 1.0
output_value: 0.0005591729091959276
expected_value: 0.0
input_value: 6.7
input_value: 3.1
input_value: 5.6
input_value: 2.4
output_value: 4.187850586900763e-06
expected_value: 0.0
output_value: 0.007092410329411652
expected_value: 0.0
output_value: 0.9954907910394163
expected_value: 1.0
input_value: 6.5
input_value: 3.0
input_value: 5.8
input_value: 2.2
output_value: 4.076798421268731e-06
expected_value: 0.0
output_value: 0.00507807509790934
expected_value: 0.0
output_value: 0.9942091813152673
expected_value: 1.0
input_value: 6.0
input_value: 3.4
input_value: 4.5
input_value: 1.6
output_value: 0.015809500861837928
expected_value: 0.0
output_value: 0.998905651780586
expected_value: 1.0
output_value: 0.0018307463837201109
expected_value: 0.0
input_value: 6.1
input_value: 2.9
input_value: 4.7
input_value: 1.4
output_value: 0.007872117359989323
expected_value: 0.0
output_value: 0.9973427251389975
expected_value: 1.0
output_value: 0.0022314859033145742
expected_value: 0.0
input_value: 6.2
input_value: 2.8
input_value: 4.8
input_value: 1.8
output_value: 3.3641190849335115e-06
expected_value: 0.0
output_value: 0.00438445237734118
expected_value: 0.0
output_value: 0.9827293789659369
expected_value: 1.0
input_value: 4.8
input_value: 3.4
input_value: 1.6
input_value: 0.2
output_value: 0.9911299642144064
expected_value: 1.0
output_value: 0.006023992685242167
expected_value: 0.0
output_value: 0.003268844277213373
expected_value: 0.0
input_value: 6.4
input_value: 2.8
input_value: 5.6
input_value: 2.1
output_value: 3.117263993826153e-06
expected_value: 0.0
output_value: 0.003640434736696793
expected_value: 0.0
output_value: 0.9925869803824523
expected_value: 1.0
input_value: 5.7
input_value: 2.9
input_value: 4.2
input_value: 1.3
output_value: 0.00881424627235982
expected_value: 0.0
output_value: 0.9973429267644704
expected_value: 1.0
output_value: 0.0009581163265326023
expected_value: 0.0
input_value: 5.4
input_value: 3.4
input_value: 1.7
input_value: 0.2
output_value: 0.992141033152487
expected_value: 1.0
output_value: 0.010976654934530095
expected_value: 0.0
output_value: 0.005330200157054697
expected_value: 0.0
input_value: 6.2
input_value: 2.2
input_value: 4.5
input_value: 1.5
output_value: 1.2699346780336642e-06
expected_value: 0.0
output_value: 0.0013895091974786462
expected_value: 1.0
output_value: 0.9818637884775105
expected_value: 0.0
input_value: 4.7
input_value: 3.2
input_value: 1.6
input_value: 0.2
output_value: 0.9891277725874187
expected_value: 1.0
output_value: 0.004874766593073116
expected_value: 0.0
output_value: 0.002600994247762632
expected_value: 0.0
input_value: 6.5
input_value: 3.0
input_value: 5.2
input_value: 2.0
output_value: 3.306391287301052e-06
expected_value: 0.0
output_value: 0.004485943788892194
expected_value: 0.0
output_value: 0.9932976852893939
expected_value: 1.0
input_value: 5.6
input_value: 2.7
input_value: 4.2
input_value: 1.3
output_value: 0.0064287005219779226
expected_value: 0.0
output_value: 0.99587683964092
expected_value: 1.0
output_value: 0.0009141698181369418
expected_value: 0.0
input_value: 5.9
input_value: 3.0
input_value: 5.1
input_value: 1.8
output_value: 3.1176782583673306e-06
expected_value: 0.0
output_value: 0.0024149241620232517
expected_value: 0.0
output_value: 0.9878029105955057
expected_value: 1.0
input_value: 5.8
input_value: 2.6
input_value: 4.0
input_value: 1.2
output_value: 0.0063953928832012254
expected_value: 0.0
output_value: 0.9966842116938713
expected_value: 1.0
output_value: 0.0008240930906762135
expected_value: 0.0
input_value: 6.6
input_value: 2.9
input_value: 4.6
input_value: 1.3
output_value: 0.0115745473147546
expected_value: 0.0
output_value: 0.9989983871401484
expected_value: 1.0
output_value: 0.002017482147536695
expected_value: 0.0
Final Testing RMSE = 0.06237313350695306


--------------------------------------------------- Run Sin
Feature: [1.22], Label: [0.93909936]
Output:  0.8858179542692455
Feature: [1.57], Label: [0.99999968]
Output:  0.912646713726127
Feature: [1.], Label: [0.84147098]
Output:  0.8654163666916717
Feature: [0.33], Label: [0.32404303]
Output:  0.7825825190498601
Feature: [0.17], Label: [0.16918235]
Output:  0.7573408357819261
Feature: [0.36], Label: [0.35227423]
Output:  0.7856305337468052
Feature: [0.53], Label: [0.50553334]
Output:  0.8088830846867074
Feature: [1.2], Label: [0.93203909]
Output:  0.8824652342271803
Feature: [1.43], Label: [0.99010456]
Output:  0.9012836355499323
Feature: [1.55], Label: [0.99978376]
Output:  0.9099848527693752
Feature: [0.11], Label: [0.1097783]
Output:  0.7460271742823521
Feature: [1.18], Label: [0.92460601]
Output:  0.8802084173863617
Feature: [0.6], Label: [0.56464247]
Output:  0.8171471949051925
Feature: [0.95], Label: [0.8134155]
Output:  0.8576768940125187
Feature: [0.38], Label: [0.37092047]
Output:  0.7866540237362417
Epoch: 0 RMSE = 0.2379549063955648
Epoch: 100 RMSE = 0.22434375473828425
Epoch: 200 RMSE = 0.2219327174575044
Epoch: 300 RMSE = 0.2183005649146389
Epoch: 400 RMSE = 0.21189649775589123
Epoch: 500 RMSE = 0.20103124445061343
Epoch: 600 RMSE = 0.1856582677904536
Epoch: 700 RMSE = 0.1688999372100119
Epoch: 800 RMSE = 0.15314278310236235
Epoch: 900 RMSE = 0.13955074339643175
Feature: [0.33], Label: [0.32404303]
Output:  0.45701523448231385
Feature: [1.57], Label: [0.99999968]
Output:  0.8603661953757497
Feature: [0.6], Label: [0.56464247]
Output:  0.5897319003047996
Feature: [1.2], Label: [0.93203909]
Output:  0.7940755769340954
Feature: [1.22], Label: [0.93909936]
Output:  0.7988646782279688
Feature: [1.], Label: [0.84147098]
Output:  0.7421225169698068
Feature: [0.17], Label: [0.16918235]
Output:  0.376120494156569
Feature: [0.38], Label: [0.37092047]
Output:  0.48275079224446604
Feature: [0.95], Label: [0.8134155]
Output:  0.7261814227451021
Feature: [1.55], Label: [0.99978376]
Output:  0.8579355277218064
Feature: [0.11], Label: [0.1097783]
Output:  0.34620131911672447
Feature: [0.53], Label: [0.50553334]
Output:  0.5568840183650609
Feature: [0.36], Label: [0.35227423]
Output:  0.47199221258864366
Feature: [1.18], Label: [0.92460601]
Output:  0.7891498737452907
Feature: [1.43], Label: [0.99010456]
Output:  0.8392169120221941
Epoch: 1000 RMSE = 0.12779520157863494
Epoch: 1100 RMSE = 0.11798830990160335
Epoch: 1200 RMSE = 0.10936063713098004
Epoch: 1300 RMSE = 0.1019053434431702
Epoch: 1400 RMSE = 0.09539489508287184
Epoch: 1500 RMSE = 0.08955667254014607
Epoch: 1600 RMSE = 0.08438682358752084
Epoch: 1700 RMSE = 0.07972633041903367
Epoch: 1800 RMSE = 0.07551419809881978
Epoch: 1900 RMSE = 0.07165222947586729
Feature: [0.95], Label: [0.8134155]
Output:  0.7795704363496847
Feature: [0.6], Label: [0.56464247]
Output:  0.5922914475393692
Feature: [1.57], Label: [0.99999968]
Output:  0.9088816083863811
Feature: [1.43], Label: [0.99010456]
Output:  0.8921262496555398
Feature: [1.18], Label: [0.92460601]
Output:  0.8477398724313749
Feature: [1.22], Label: [0.93909936]
Output:  0.8565951268911065
Feature: [0.17], Label: [0.16918235]
Output:  0.259198965217035
Feature: [0.38], Label: [0.37092047]
Output:  0.4216815729981227
Feature: [0.33], Label: [0.32404303]
Output:  0.3808517303342966
Feature: [0.36], Label: [0.35227423]
Output:  0.4050393345409101
Feature: [1.], Label: [0.84147098]
Output:  0.7972828865575255
Feature: [0.53], Label: [0.50553334]
Output:  0.5408622386881119
Feature: [1.55], Label: [0.99978376]
Output:  0.9067166944527245
Feature: [0.11], Label: [0.1097783]
Output:  0.21908209789572083
Feature: [1.2], Label: [0.93203909]
Output:  0.8519510003123958
Epoch: 2000 RMSE = 0.06815255122265297
Epoch: 2100 RMSE = 0.06495083292709695
Epoch: 2200 RMSE = 0.06194664763703517
Epoch: 2300 RMSE = 0.05923391924155866
Epoch: 2400 RMSE = 0.056729658865317466
Epoch: 2500 RMSE = 0.05438695695618135
Epoch: 2600 RMSE = 0.05220208192972991
Epoch: 2700 RMSE = 0.050237196749863225
Epoch: 2800 RMSE = 0.04828273085248662
Epoch: 2900 RMSE = 0.0465012163241146
Feature: [0.33], Label: [0.32404303]
Output:  0.34999623401829977
Feature: [1.2], Label: [0.93203909]
Output:  0.8757871407838571
Feature: [1.57], Label: [0.99999968]
Output:  0.9281774388380971
Feature: [1.43], Label: [0.99010456]
Output:  0.913282627733254
Feature: [1.], Label: [0.84147098]
Output:  0.8214028020009676
Feature: [0.17], Label: [0.16918235]
Output:  0.21770267970365406
Feature: [0.95], Label: [0.8134155]
Output:  0.8029256565042164
Feature: [0.38], Label: [0.37092047]
Output:  0.39635252244986674
Feature: [1.22], Label: [0.93909936]
Output:  0.8800207183975731
Feature: [0.53], Label: [0.50553334]
Output:  0.5348176133824089
Feature: [0.6], Label: [0.56464247]
Output:  0.5942745567896975
Feature: [1.18], Label: [0.92460601]
Output:  0.8715147332599237
Feature: [1.55], Label: [0.99978376]
Output:  0.9263373924771366
Feature: [0.36], Label: [0.35227423]
Output:  0.37772511253596763
Feature: [0.11], Label: [0.1097783]
Output:  0.1771411070386
Epoch: 3000 RMSE = 0.04484707147242865
Epoch: 3100 RMSE = 0.04324573252623656
Epoch: 3200 RMSE = 0.04182565651209076
Epoch: 3300 RMSE = 0.04040408859601859
Epoch: 3400 RMSE = 0.0391260923605585
Epoch: 3500 RMSE = 0.037899515017381466
Epoch: 3600 RMSE = 0.03670082498353762
Epoch: 3700 RMSE = 0.03559520655660194
Epoch: 3800 RMSE = 0.0346257132334026
Epoch: 3900 RMSE = 0.03371164373682235
Feature: [1.22], Label: [0.93909936]
Output:  0.8928270294541105
Feature: [1.55], Label: [0.99978376]
Output:  0.9368896445918371
Feature: [0.95], Label: [0.8134155]
Output:  0.8156743784724297
Feature: [1.], Label: [0.84147098]
Output:  0.8344757700954871
Feature: [0.6], Label: [0.56464247]
Output:  0.595188171415447
Feature: [0.33], Label: [0.32404303]
Output:  0.33399388914254574
Feature: [0.11], Label: [0.1097783]
Output:  0.1579315996001787
Feature: [1.2], Label: [0.93203909]
Output:  0.8887788186858961
Feature: [0.36], Label: [0.35227423]
Output:  0.3629962105887953
Feature: [1.43], Label: [0.99010456]
Output:  0.9246969476800828
Feature: [0.38], Label: [0.37092047]
Output:  0.3827312320340509
Feature: [0.53], Label: [0.50553334]
Output:  0.5308808487439131
Feature: [0.17], Label: [0.16918235]
Output:  0.19788240385155426
Feature: [1.57], Label: [0.99999968]
Output:  0.9385562431922938
Feature: [1.18], Label: [0.92460601]
Output:  0.884543637766263
Epoch: 4000 RMSE = 0.032921625931143804
Epoch: 4100 RMSE = 0.03218132051394202
Epoch: 4200 RMSE = 0.03143221405406275
Epoch: 4300 RMSE = 0.030744393084953123
Epoch: 4400 RMSE = 0.03006537393912189
Epoch: 4500 RMSE = 0.029437376820225236
Epoch: 4600 RMSE = 0.028789798296711487
Epoch: 4700 RMSE = 0.028250239214272728
Epoch: 4800 RMSE = 0.02771331709523856
Epoch: 4900 RMSE = 0.02719146974158485
Feature: [0.11], Label: [0.1097783]
Output:  0.14785697499988987
Feature: [1.2], Label: [0.93203909]
Output:  0.8968058155173132
Feature: [1.43], Label: [0.99010456]
Output:  0.9318287889226538
Feature: [1.18], Label: [0.92460601]
Output:  0.8926921604475556
Feature: [1.], Label: [0.84147098]
Output:  0.8425194274736412
Feature: [0.95], Label: [0.8134155]
Output:  0.8234605030005555
Feature: [1.55], Label: [0.99978376]
Output:  0.9434766977754555
Feature: [1.22], Label: [0.93909936]
Output:  0.9008724064147248
Feature: [0.36], Label: [0.35227423]
Output:  0.35455390226416283
Feature: [0.38], Label: [0.37092047]
Output:  0.3748058371288416
Feature: [0.33], Label: [0.32404303]
Output:  0.32477020857874034
Feature: [0.6], Label: [0.56464247]
Output:  0.5954319761749728
Feature: [1.57], Label: [0.99999968]
Output:  0.945106326823185
Feature: [0.17], Label: [0.16918235]
Output:  0.18739415191244013
Feature: [0.53], Label: [0.50553334]
Output:  0.5283998959479274
Epoch: 5000 RMSE = 0.02685216390324685
Epoch: 5100 RMSE = 0.026395354159832456
Epoch: 5200 RMSE = 0.026131698463999094
Epoch: 5300 RMSE = 0.02582244042129837
Epoch: 5400 RMSE = 0.025625758187587937
Epoch: 5500 RMSE = 0.025442427337810943
Epoch: 5600 RMSE = 0.02527595284681734
Epoch: 5700 RMSE = 0.02512516258630202
Epoch: 5800 RMSE = 0.025020869846053517
Epoch: 5900 RMSE = 0.02492189794125518
Feature: [1.22], Label: [0.93909936]
Output:  0.9060895700317392
Feature: [1.2], Label: [0.93203909]
Output:  0.9021864215179987
Feature: [1.], Label: [0.84147098]
Output:  0.847703981735786
Feature: [1.55], Label: [0.99978376]
Output:  0.9479370260406859
Feature: [0.53], Label: [0.50553334]
Output:  0.5264642765801993
Feature: [1.18], Label: [0.92460601]
Output:  0.8980271997990042
Feature: [1.57], Label: [0.99999968]
Output:  0.9495195128413451
Feature: [0.6], Label: [0.56464247]
Output:  0.5950992227786409
Feature: [1.43], Label: [0.99010456]
Output:  0.9366393019140105
Feature: [0.33], Label: [0.32404303]
Output:  0.3188414772719438
Feature: [0.11], Label: [0.1097783]
Output:  0.1422893085323056
Feature: [0.95], Label: [0.8134155]
Output:  0.8283870403889253
Feature: [0.17], Label: [0.16918235]
Output:  0.18127914051092453
Feature: [0.36], Label: [0.35227423]
Output:  0.34885599977613635
Feature: [0.38], Label: [0.37092047]
Output:  0.36940488926180565
Epoch: 6000 RMSE = 0.024837920747094226
Epoch: 6100 RMSE = 0.024735717887080604
Epoch: 6200 RMSE = 0.024641630729291344
Epoch: 6300 RMSE = 0.024563241190178105
Epoch: 6400 RMSE = 0.02447619791250772
Epoch: 6500 RMSE = 0.024382846655996604
Epoch: 6600 RMSE = 0.024308661819988264
Epoch: 6700 RMSE = 0.024237478473785743
Epoch: 6800 RMSE = 0.024163613955335072
Epoch: 6900 RMSE = 0.02409386422949024
Feature: [1.], Label: [0.84147098]
Output:  0.8511194850724293
Feature: [0.11], Label: [0.1097783]
Output:  0.1391091563139133
Feature: [0.53], Label: [0.50553334]
Output:  0.5245847922060333
Feature: [1.22], Label: [0.93909936]
Output:  0.9097282519721627
Feature: [0.36], Label: [0.35227423]
Output:  0.34521197966250544
Feature: [1.2], Label: [0.93203909]
Output:  0.9058406451485865
Feature: [1.43], Label: [0.99010456]
Output:  0.9400598845608563
Feature: [0.33], Label: [0.32404303]
Output:  0.31508464317296775
Feature: [1.18], Label: [0.92460601]
Output:  0.9017523641438275
Feature: [0.17], Label: [0.16918235]
Output:  0.17782091900216665
Feature: [0.38], Label: [0.37092047]
Output:  0.36605965920770334
Feature: [1.57], Label: [0.99999968]
Output:  0.9526986344825888
Feature: [0.95], Label: [0.8134155]
Output:  0.8317617427718346
Feature: [1.55], Label: [0.99978376]
Output:  0.9511542206740692
Feature: [0.6], Label: [0.56464247]
Output:  0.5945620941387029
Epoch: 7000 RMSE = 0.02401434304094089
Epoch: 7100 RMSE = 0.023940135860051247
Epoch: 7200 RMSE = 0.023878670605314643
Epoch: 7300 RMSE = 0.023809564307970554
Epoch: 7400 RMSE = 0.02373438055548056
Epoch: 7500 RMSE = 0.023681518143450687
Epoch: 7600 RMSE = 0.023614786958649568
Epoch: 7700 RMSE = 0.02355263975895205
Epoch: 7800 RMSE = 0.02350119171176011
Epoch: 7900 RMSE = 0.02345108784244582
Feature: [0.53], Label: [0.50553334]
Output:  0.5232344578847343
Feature: [0.17], Label: [0.16918235]
Output:  0.1757250525261616
Feature: [1.22], Label: [0.93909936]
Output:  0.9124247441106466
Feature: [1.18], Label: [0.92460601]
Output:  0.9043619690909602
Feature: [0.95], Label: [0.8134155]
Output:  0.8338301082036647
Feature: [1.43], Label: [0.99010456]
Output:  0.9425931355036455
Feature: [0.11], Label: [0.1097783]
Output:  0.1373918359508758
Feature: [0.38], Label: [0.37092047]
Output:  0.36354521912653937
Feature: [1.2], Label: [0.93203909]
Output:  0.9085327376839649
Feature: [1.57], Label: [0.99999968]
Output:  0.9550623157604372
Feature: [0.36], Label: [0.35227423]
Output:  0.3429326132987769
Feature: [1.55], Label: [0.99978376]
Output:  0.9535616221944335
Feature: [1.], Label: [0.84147098]
Output:  0.8535853210830603
Feature: [0.6], Label: [0.56464247]
Output:  0.5938016132317419
Feature: [0.33], Label: [0.32404303]
Output:  0.31257636821729784
Epoch: 8000 RMSE = 0.023388326868522498
Epoch: 8100 RMSE = 0.023332957891741824
Epoch: 8200 RMSE = 0.023280495564252716
Epoch: 8300 RMSE = 0.023231127677745045
Epoch: 8400 RMSE = 0.023175777096692763
Epoch: 8500 RMSE = 0.023121504679425153
Epoch: 8600 RMSE = 0.023072985945632434
Epoch: 8700 RMSE = 0.02303000668978998
Epoch: 8800 RMSE = 0.022986965801810928
Epoch: 8900 RMSE = 0.022929703404971715
Feature: [0.17], Label: [0.16918235]
Output:  0.1746756143294167
Feature: [0.6], Label: [0.56464247]
Output:  0.5929433446366648
Feature: [1.55], Label: [0.99978376]
Output:  0.9553833967221406
Feature: [0.38], Label: [0.37092047]
Output:  0.36186572330661826
Feature: [0.95], Label: [0.8134155]
Output:  0.8352962007569861
Feature: [0.33], Label: [0.32404303]
Output:  0.3108998140862128
Feature: [1.22], Label: [0.93909936]
Output:  0.9144336539165697
Feature: [0.53], Label: [0.50553334]
Output:  0.5219915871002195
Feature: [1.18], Label: [0.92460601]
Output:  0.9063108620146422
Feature: [1.2], Label: [0.93203909]
Output:  0.9105004748151797
Feature: [1.43], Label: [0.99010456]
Output:  0.9445642826520465
Feature: [0.36], Label: [0.35227423]
Output:  0.34125413749882005
Feature: [1.57], Label: [0.99999968]
Output:  0.9569275459688124
Feature: [1.], Label: [0.84147098]
Output:  0.8552247580136335
Feature: [0.11], Label: [0.1097783]
Output:  0.136560017785233
Epoch: 9000 RMSE = 0.022893258051694163
Epoch: 9100 RMSE = 0.02284337784911691
Epoch: 9200 RMSE = 0.022797645340684045
Epoch: 9300 RMSE = 0.022752703919543545
Epoch: 9400 RMSE = 0.022711860514516458
Epoch: 9500 RMSE = 0.022673197876602016
Epoch: 9600 RMSE = 0.022642191278398702
Epoch: 9700 RMSE = 0.022588988742373077
Epoch: 9800 RMSE = 0.022553581604440636
Epoch: 9900 RMSE = 0.02251923020166235
Feature: [0.6], Label: [0.56464247]
Output:  0.5921963780855894
Feature: [0.36], Label: [0.35227423]
Output:  0.33997702248369477
Feature: [0.11], Label: [0.1097783]
Output:  0.13615686664964696
Feature: [1.2], Label: [0.93203909]
Output:  0.9120061805795119
Feature: [0.33], Label: [0.32404303]
Output:  0.3098504191424664
Feature: [0.53], Label: [0.50553334]
Output:  0.5209560011299699
Feature: [0.95], Label: [0.8134155]
Output:  0.836296194965004
Feature: [0.38], Label: [0.37092047]
Output:  0.36060150193348806
Feature: [1.18], Label: [0.92460601]
Output:  0.9078063859395394
Feature: [0.17], Label: [0.16918235]
Output:  0.17407388576812227
Feature: [1.55], Label: [0.99978376]
Output:  0.9568809417036184
Feature: [1.], Label: [0.84147098]
Output:  0.8563028979499905
Feature: [1.22], Label: [0.93909936]
Output:  0.9159538404649631
Feature: [1.57], Label: [0.99999968]
Output:  0.9583806380397167
Feature: [1.43], Label: [0.99010456]
Output:  0.9461124826936855
Epoch: 10000 RMSE = 0.02248400338012931
Training finished.
 Final Training RMSE = 0.02248400338012931 

----- starting test
input_value: 1.26
output_value: 0.9232340903989134
expected_value: 0.952090341590516
input_value: 0.92
output_value: 0.8229127921136464
expected_value: 0.795601620036366
input_value: 1.4
output_value: 0.9428407373412423
expected_value: 0.98544972998846
input_value: 1.27
output_value: 0.9249113409130452
expected_value: 0.955100855584692
input_value: 0.62
output_value: 0.611461852523569
expected_value: 0.581035160537305
input_value: 0.9
output_value: 0.8132597577731971
expected_value: 0.783326909627483
input_value: 0.04
output_value: 0.10073359033146548
expected_value: 0.0399893341866342
input_value: 0.42
output_value: 0.4031164533192678
expected_value: 0.40776045305957
input_value: 0.16
output_value: 0.16729516211785597
expected_value: 0.159318206614246
input_value: 1.08
output_value: 0.8827209424510766
expected_value: 0.881957806884948
input_value: 0.66
output_value: 0.6482297011309893
expected_value: 0.613116851973434
input_value: 0.98
output_value: 0.8487252787627704
expected_value: 0.83049737049197
input_value: 1.3
output_value: 0.9296597740904465
expected_value: 0.963558185417193
input_value: 0.14
output_value: 0.15424767782330917
expected_value: 0.139543114644236
input_value: 1.34
output_value: 0.9353843818831994
expected_value: 0.973484541695319
input_value: 0.93
output_value: 0.8275349562315674
expected_value: 0.801619940883777
input_value: 0.49
output_value: 0.4784668192221681
expected_value: 0.470625888171158
input_value: 0.71
output_value: 0.6905760816567251
expected_value: 0.651833771021537
input_value: 1.23
output_value: 0.9178967437402971
expected_value: 0.942488801931697
input_value: 1.32
output_value: 0.9326041109408666
expected_value: 0.968715100118265
input_value: 0.45
output_value: 0.4353727584185964
expected_value: 0.43496553411123
input_value: 0.39
output_value: 0.37125879915002225
expected_value: 0.380188415123161
input_value: 1.56
output_value: 0.9576642304776294
expected_value: 0.999941720229966
input_value: 0.67
output_value: 0.6570301941747395
expected_value: 0.62098598703656
input_value: 0.72
output_value: 0.6985392288749663
expected_value: 0.659384671971473
input_value: 0.84
output_value: 0.780818395581016
expected_value: 0.744643119970859
input_value: 0.88
output_value: 0.8030417102408344
expected_value: 0.770738878898969
input_value: 1.06
output_value: 0.876713980249958
expected_value: 0.872355482344986
input_value: 0.48
output_value: 0.46771821969848243
expected_value: 0.461779175541483
input_value: 0.54
output_value: 0.5314740826113336
expected_value: 0.514135991653113
input_value: 0.43
output_value: 0.41383950844232925
expected_value: 0.416870802429211
input_value: 0.31
output_value: 0.29048378937844693
expected_value: 0.305058636443443
input_value: 0.78
output_value: 0.742711851448267
expected_value: 0.70327941920041
input_value: 0.23
output_value: 0.21937999910469538
expected_value: 0.227977523535188
input_value: 1.11
output_value: 0.8910782369832466
expected_value: 0.895698685680048
input_value: 0.02
output_value: 0.09220329749904471
expected_value: 0.0199986666933331
input_value: 0.1
output_value: 0.1305585927355605
expected_value: 0.0998334166468282
input_value: 0.46
output_value: 0.4461599347262751
expected_value: 0.44394810696552
input_value: 1.33
output_value: 0.9340140936940272
expected_value: 0.971148377921045
input_value: 0.89
output_value: 0.8082228434229705
expected_value: 0.777071747526824
input_value: 1.51
output_value: 0.9536883458934872
expected_value: 0.998152472497548
input_value: 1.14
output_value: 0.8987126656983554
expected_value: 0.908633496115883
input_value: 0.22
output_value: 0.21133329879480287
expected_value: 0.218229623080869
input_value: 1.1
output_value: 0.8883760977763252
expected_value: 0.891207360061435
input_value: 0.51
output_value: 0.49984812295105785
expected_value: 0.488177246882907
input_value: 1.45
output_value: 0.9481724660797015
expected_value: 0.992712991037588
input_value: 1.41
output_value: 0.9439664510647534
expected_value: 0.98710010101385
input_value: 1.29
output_value: 0.9281226658430773
expected_value: 0.960835064206073
input_value: 1.53
output_value: 0.955340835642985
expected_value: 0.999167945271476
input_value: 0.83
output_value: 0.7748745385235244
expected_value: 0.737931371109963
input_value: 0.41
output_value: 0.3924377550135576
expected_value: 0.398609327984423
input_value: 0.03
output_value: 0.0963848918394144
expected_value: 0.0299955002024957
input_value: 0.01
output_value: 0.08818452908743378
expected_value: 0.00999983333416666
input_value: 0.15
output_value: 0.16066981488969986
expected_value: 0.149438132473599
input_value: 0.55
output_value: 0.541857854606612
expected_value: 0.522687228930659
input_value: 1.36
output_value: 0.9380109073886919
expected_value: 0.977864602435316
input_value: 0.3
output_value: 0.2809887134963804
expected_value: 0.29552020666134
input_value: 0.52
output_value: 0.5104596728472
expected_value: 0.496880137843737
input_value: 0.77
output_value: 0.7357778537944977
expected_value: 0.696135238627357
input_value: 0.07
output_value: 0.11482340815032153
expected_value: 0.0699428473375328
input_value: 0.29
output_value: 0.2716549128939247
expected_value: 0.285952225104836
input_value: 0.0
output_value: 0.08432422678113306
expected_value: 0.0
input_value: 1.54
output_value: 0.9561353682864215
expected_value: 0.999525830605479
input_value: 0.4
output_value: 0.3818147922752361
expected_value: 0.389418342308651
input_value: 0.81
output_value: 0.7625042222126436
expected_value: 0.724287174370143
input_value: 0.63
output_value: 0.6208807480222323
expected_value: 0.58914475794227
input_value: 0.64
output_value: 0.6301512537070075
expected_value: 0.597195441362392
input_value: 1.01
output_value: 0.8600140357174703
expected_value: 0.846831844618015
input_value: 0.47
output_value: 0.4569455330825262
expected_value: 0.452886285379068
input_value: 0.65
output_value: 0.6392688951825464
expected_value: 0.60518640573604
input_value: 1.37
output_value: 0.9392695590504719
expected_value: 0.979908061398614
input_value: 1.13
output_value: 0.8962441138651215
expected_value: 0.904412189378826
input_value: 1.44
output_value: 0.9471636122087331
expected_value: 0.991458348191686
input_value: 0.13
output_value: 0.14802740767002026
expected_value: 0.129634142619695
input_value: 1.42
output_value: 0.9450615267679295
expected_value: 0.98865176285172
input_value: 0.05
output_value: 0.10525356805648393
expected_value: 0.0499791692706783
input_value: 0.79
output_value: 0.7494766084947331
expected_value: 0.710353272417608
input_value: 0.19
output_value: 0.18839738719960616
expected_value: 0.188858894976501
input_value: 0.68
output_value: 0.6656673794373434
expected_value: 0.628793024018469
input_value: 0.06
output_value: 0.10994887420031937
expected_value: 0.0599640064794446
input_value: 1.24
output_value: 0.9197284589845607
expected_value: 0.945783999449539
input_value: 0.58
output_value: 0.5724097574153701
expected_value: 0.548023936791874
input_value: 0.26
output_value: 0.24468646854050297
expected_value: 0.257080551892155
input_value: 0.74
output_value: 0.713950362267969
expected_value: 0.674287911628145
input_value: 0.61
output_value: 0.6018995512741034
expected_value: 0.572867460100481
input_value: 0.75
output_value: 0.7213978323626854
expected_value: 0.681638760023334
input_value: 1.39
output_value: 0.9416833820543263
expected_value: 0.983700814811277
input_value: 1.5
output_value: 0.9528290325629272
expected_value: 0.997494986604054
input_value: 1.04
output_value: 0.8703336717619561
expected_value: 0.862404227243338
input_value: 1.16
output_value: 0.903432587296921
expected_value: 0.916803108771767
input_value: 1.52
output_value: 0.9545253836852302
expected_value: 0.998710143975583
input_value: 0.08
output_value: 0.11988089452535827
expected_value: 0.0799146939691727
input_value: 0.86
output_value: 0.7922353001384935
expected_value: 0.757842562895277
input_value: 1.03
output_value: 0.8669965517730274
expected_value: 0.857298989188603
input_value: 0.73
output_value: 0.7063308015662882
expected_value: 0.666869635003698
input_value: 1.09
output_value: 0.8855911839732038
expected_value: 0.886626914449487
input_value: 0.35
output_value: 0.32992135899609937
expected_value: 0.342897807455451
input_value: 0.27
output_value: 0.25349783912777385
expected_value: 0.266731436688831
input_value: 0.18
output_value: 0.18115871609122522
expected_value: 0.179029573425824
input_value: 1.19
output_value: 0.9100025111039999
expected_value: 0.928368967249167
input_value: 1.05
output_value: 0.8735718738563786
expected_value: 0.867423225594017
input_value: 0.32
output_value: 0.3001327627075247
expected_value: 0.314566560616118
input_value: 0.96
output_value: 0.8406208834307342
expected_value: 0.819191568300998
input_value: 0.7
output_value: 0.6824421768790526
expected_value: 0.644217687237691
input_value: 1.25
output_value: 0.9215070101863423
expected_value: 0.948984619355586
input_value: 1.28
output_value: 0.9265403523600324
expected_value: 0.958015860289225
input_value: 0.87
output_value: 0.7977134675004323
expected_value: 0.764328937025505
input_value: 1.38
output_value: 0.9404933471655635
expected_value: 0.98185353037236
input_value: 0.09
output_value: 0.12512485724132455
expected_value: 0.089878549198011
input_value: 1.47
output_value: 0.9501101773292252
expected_value: 0.994924349777581
input_value: 0.25
output_value: 0.23606015936133523
expected_value: 0.247403959254523
input_value: 0.37
output_value: 0.3503916334527139
expected_value: 0.361615431964962
input_value: 1.15
output_value: 0.9011080705483335
expected_value: 0.912763940260521
input_value: 0.28
output_value: 0.26248920663168135
expected_value: 0.276355648564114
input_value: 0.34
output_value: 0.31986022137872827
expected_value: 0.333487092140814
input_value: 0.57
output_value: 0.5623339359812839
expected_value: 0.539632048733969
input_value: 0.56
output_value: 0.5521472982426077
expected_value: 0.531186197920883
input_value: 0.76
output_value: 0.7286734710011652
expected_value: 0.688921445110551
input_value: 1.21
output_value: 0.9140667837379973
expected_value: 0.935616001553386
input_value: 0.21
output_value: 0.20348597399592766
expected_value: 0.2084598998461
input_value: 0.2
output_value: 0.1958401482253782
expected_value: 0.198669330795061
input_value: 1.31
output_value: 0.9311531226244488
expected_value: 0.966184951612734
input_value: 0.59
output_value: 0.58236723595939
expected_value: 0.556361022912784
input_value: 1.02
output_value: 0.8635576443546715
expected_value: 0.852108021949363
input_value: 0.82
output_value: 0.7687705497352003
expected_value: 0.731145829726896
input_value: 0.5
output_value: 0.4891803609934285
expected_value: 0.479425538604203
input_value: 1.46
output_value: 0.9491543722269324
expected_value: 0.993868363411645
input_value: 1.07
output_value: 0.8797627631368697
expected_value: 0.877200504274682
input_value: 0.97
output_value: 0.8447329770206188
expected_value: 0.82488571333845
input_value: 0.69
output_value: 0.6741387310532606
expected_value: 0.636537182221968
input_value: 0.99
output_value: 0.8526008601337787
expected_value: 0.836025978600521
input_value: 0.94
output_value: 0.8320249673600407
expected_value: 0.807558100405114
input_value: 1.17
output_value: 0.9056884155937801
expected_value: 0.920750597736136
input_value: 0.85
output_value: 0.7866044829397776
expected_value: 0.751280405140293
input_value: 0.91
output_value: 0.8181554063573345
expected_value: 0.78950373968995
input_value: 0.44
output_value: 0.4245954481678113
expected_value: 0.425939465066
input_value: 1.35
output_value: 0.9367162440364706
expected_value: 0.975723357826659
input_value: 1.49
output_value: 0.9519467299933494
expected_value: 0.996737752043143
input_value: 0.24
output_value: 0.22762337912586902
expected_value: 0.237702626427135
input_value: 0.8
output_value: 0.7560735222631926
expected_value: 0.717356090899523
input_value: 1.48
output_value: 0.9510406996548535
expected_value: 0.99588084453764
input_value: 0.12
output_value: 0.1420072650576616
expected_value: 0.119712207288919
input_value: 1.12
output_value: 0.8937000968091886
expected_value: 0.900100442176505
Final Testing RMSE = 0.026362785859323095


--------------------------------------------------- Run XOR
Feature: [1. 0.], Label: [1.]
Output:  0.9158184027351421
Feature: [1. 1.], Label: [0.]
Output:  0.9555680716663142
Feature: [0. 0.], Label: [0.]
Output:  0.7600226523116627
Feature: [0. 1.], Label: [1.]
Output:  0.8641970663427555
Feature: [1. 1.], Label: [0.]
Output:  0.9549215039294169
Feature: [0. 0.], Label: [0.]
Output:  0.7580127007595759
Feature: [1. 1.], Label: [0.]
Output:  0.9541893860763506
Feature: [0. 0.], Label: [0.]
Output:  0.755762461616402
Feature: [1. 0.], Label: [1.]
Output:  0.9124585963074653
Feature: [1. 1.], Label: [0.]
Output:  0.9534745527642222
Feature: [1. 1.], Label: [0.]
Output:  0.9532425432885736
Feature: [0. 0.], Label: [0.]
Output:  0.7529119679197325
Feature: [0. 1.], Label: [1.]
Output:  0.8587213871073129
Feature: [0. 1.], Label: [1.]
Output:  0.8589090706340407
Feature: [0. 1.], Label: [1.]
Output:  0.8590961152040413
Feature: [1. 0.], Label: [1.]
Output:  0.9112947843456043
Epoch: 0 RMSE = 0.5386006511034931
Epoch: 100 RMSE = 0.5056441008926569
Epoch: 200 RMSE = 0.5043556442794805
Epoch: 300 RMSE = 0.5043093544081766
Epoch: 400 RMSE = 0.500995462510561
Epoch: 500 RMSE = 0.49829495605653756
Epoch: 600 RMSE = 0.49466758664093435
Epoch: 700 RMSE = 0.486273177626736
Epoch: 800 RMSE = 0.4751642712273811
Epoch: 900 RMSE = 0.45881228264238044
Feature: [0. 1.], Label: [1.]
Output:  0.610495784586783
Feature: [1. 0.], Label: [1.]
Output:  0.22495191358267783
Feature: [0. 1.], Label: [1.]
Output:  0.6145427250767407
Feature: [0. 0.], Label: [0.]
Output:  0.3261422282036357
Feature: [0. 1.], Label: [1.]
Output:  0.6151646593603488
Feature: [0. 0.], Label: [0.]
Output:  0.3263084537837534
Feature: [0. 0.], Label: [0.]
Output:  0.3253236529594184
Feature: [1. 1.], Label: [0.]
Output:  0.3843417758405414
Feature: [1. 1.], Label: [0.]
Output:  0.3812089740504167
Feature: [1. 0.], Label: [1.]
Output:  0.22305526516239532
Feature: [0. 0.], Label: [0.]
Output:  0.32347113906518227
Feature: [1. 1.], Label: [0.]
Output:  0.3809616243971567
Feature: [1. 1.], Label: [0.]
Output:  0.37787842468857236
Feature: [1. 0.], Label: [1.]
Output:  0.22099061059532385
Feature: [1. 1.], Label: [0.]
Output:  0.379095879242266
Feature: [0. 1.], Label: [1.]
Output:  0.6091119874174905
Epoch: 1000 RMSE = 0.4429012004030739
Epoch: 1100 RMSE = 0.4278642621489481
Epoch: 1200 RMSE = 0.41386309211354
Epoch: 1300 RMSE = 0.40346083227880497
Epoch: 1400 RMSE = 0.3956420386680339
Epoch: 1500 RMSE = 0.3904408109189564
Epoch: 1600 RMSE = 0.3862980746403225
Epoch: 1700 RMSE = 0.38720682485211766
Epoch: 1800 RMSE = 0.3862012659657025
Epoch: 1900 RMSE = 0.3834605201836954
Feature: [0. 0.], Label: [0.]
Output:  0.4157329735675722
Feature: [0. 0.], Label: [0.]
Output:  0.4142007792980256
Feature: [1. 0.], Label: [1.]
Output:  0.35318496609918254
Feature: [1. 0.], Label: [1.]
Output:  0.3594487976341992
Feature: [0. 1.], Label: [1.]
Output:  0.7494859726894579
Feature: [0. 1.], Label: [1.]
Output:  0.7499317719573805
Feature: [1. 1.], Label: [0.]
Output:  0.29602225510441316
Feature: [0. 0.], Label: [0.]
Output:  0.41969378374305566
Feature: [1. 1.], Label: [0.]
Output:  0.29184057641288347
Feature: [1. 0.], Label: [1.]
Output:  0.3600502752695611
Feature: [1. 1.], Label: [0.]
Output:  0.2947759834947036
Feature: [0. 1.], Label: [1.]
Output:  0.7488293318733662
Feature: [0. 1.], Label: [1.]
Output:  0.749277632148661
Feature: [0. 0.], Label: [0.]
Output:  0.42011082776325626
Feature: [1. 1.], Label: [0.]
Output:  0.29209117995452494
Feature: [1. 1.], Label: [0.]
Output:  0.2899179659703932
Epoch: 2000 RMSE = 0.37901109860231386
Epoch: 2100 RMSE = 0.367196162887791
Epoch: 2200 RMSE = 0.35366094751940236
Epoch: 2300 RMSE = 0.33782576354715593
Epoch: 2400 RMSE = 0.3242001420228801
Epoch: 2500 RMSE = 0.3114318065100671
Epoch: 2600 RMSE = 0.29974924618453963
Epoch: 2700 RMSE = 0.2896799891404185
Epoch: 2800 RMSE = 0.2806859072198864
Epoch: 2900 RMSE = 0.27289012599027845
Feature: [0. 0.], Label: [0.]
Output:  0.47034764704041254
Feature: [1. 0.], Label: [1.]
Output:  0.6138478063760836
Feature: [0. 1.], Label: [1.]
Output:  0.8458878936767138
Feature: [0. 0.], Label: [0.]
Output:  0.471354966526774
Feature: [1. 1.], Label: [0.]
Output:  0.11826177640483963
Feature: [0. 0.], Label: [0.]
Output:  0.46923990078507766
Feature: [1. 1.], Label: [0.]
Output:  0.1168870283709145
Feature: [1. 1.], Label: [0.]
Output:  0.11664920871977084
Feature: [1. 0.], Label: [1.]
Output:  0.6109774102610105
Feature: [1. 1.], Label: [0.]
Output:  0.11808970199392073
Feature: [0. 0.], Label: [0.]
Output:  0.46920884520207456
Feature: [0. 1.], Label: [1.]
Output:  0.8444182143811323
Feature: [1. 0.], Label: [1.]
Output:  0.6123522406505674
Feature: [0. 1.], Label: [1.]
Output:  0.8455506216995524
Feature: [1. 1.], Label: [0.]
Output:  0.1187490815658945
Feature: [0. 1.], Label: [1.]
Output:  0.8455822277460512
Epoch: 3000 RMSE = 0.26563573386366046
Epoch: 3100 RMSE = 0.25912407265784954
Epoch: 3200 RMSE = 0.25345375154740374
Epoch: 3300 RMSE = 0.24793661834682418
Epoch: 3400 RMSE = 0.24284380958895607
Epoch: 3500 RMSE = 0.23753345835225878
Epoch: 3600 RMSE = 0.23159800666908484
Epoch: 3700 RMSE = 0.22518767268693468
Epoch: 3800 RMSE = 0.2172669403555076
Epoch: 3900 RMSE = 0.20744133551026123
Feature: [0. 1.], Label: [1.]
Output:  0.8752581752019354
Feature: [1. 0.], Label: [1.]
Output:  0.7219570037491285
Feature: [1. 1.], Label: [0.]
Output:  0.09869536781463836
Feature: [0. 1.], Label: [1.]
Output:  0.8757239680954573
Feature: [1. 0.], Label: [1.]
Output:  0.7240755009287453
Feature: [0. 1.], Label: [1.]
Output:  0.8762652124034024
Feature: [1. 1.], Label: [0.]
Output:  0.0995005488283004
Feature: [0. 0.], Label: [0.]
Output:  0.32902330379309636
Feature: [1. 1.], Label: [0.]
Output:  0.09886912202629268
Feature: [0. 0.], Label: [0.]
Output:  0.3278755480320191
Feature: [0. 0.], Label: [0.]
Output:  0.3268811315547906
Feature: [1. 1.], Label: [0.]
Output:  0.09776633808153401
Feature: [1. 1.], Label: [0.]
Output:  0.0976303137120053
Feature: [0. 0.], Label: [0.]
Output:  0.32560773143029625
Feature: [1. 0.], Label: [1.]
Output:  0.7195373601164361
Feature: [0. 1.], Label: [1.]
Output:  0.8750747460949929
Epoch: 4000 RMSE = 0.1958723399176797
Epoch: 4100 RMSE = 0.18345499336492735
Epoch: 4200 RMSE = 0.17141185525342287
Epoch: 4300 RMSE = 0.16036159793103427
Epoch: 4400 RMSE = 0.15058869493641738
Epoch: 4500 RMSE = 0.14180056576595218
Epoch: 4600 RMSE = 0.13397580030153936
Epoch: 4700 RMSE = 0.12697912014121132
Epoch: 4800 RMSE = 0.12071060439902084
Epoch: 4900 RMSE = 0.11513600073158328
Feature: [0. 1.], Label: [1.]
Output:  0.9047941388553181
Feature: [0. 1.], Label: [1.]
Output:  0.9048663485012413
Feature: [1. 0.], Label: [1.]
Output:  0.8657057731558171
Feature: [1. 1.], Label: [0.]
Output:  0.08965670210736656
Feature: [1. 1.], Label: [0.]
Output:  0.08956494411539488
Feature: [1. 1.], Label: [0.]
Output:  0.08947344047556972
Feature: [1. 0.], Label: [1.]
Output:  0.865704784447015
Feature: [0. 0.], Label: [0.]
Output:  0.13287577979397777
Feature: [0. 1.], Label: [1.]
Output:  0.9048804557228606
Feature: [0. 0.], Label: [0.]
Output:  0.13280552897530257
Feature: [0. 0.], Label: [0.]
Output:  0.13269547416337493
Feature: [1. 0.], Label: [1.]
Output:  0.8656328777023774
Feature: [1. 1.], Label: [0.]
Output:  0.08954357561579147
Feature: [0. 1.], Label: [1.]
Output:  0.9048667521126901
Feature: [0. 0.], Label: [0.]
Output:  0.13272943429895598
Feature: [1. 1.], Label: [0.]
Output:  0.08943286134640314
Epoch: 5000 RMSE = 0.11014541314967609
Epoch: 5100 RMSE = 0.10563341941777296
Epoch: 5200 RMSE = 0.10156931253561384
Epoch: 5300 RMSE = 0.09788379235463009
Epoch: 5400 RMSE = 0.09454248023354836
Epoch: 5500 RMSE = 0.0914907056058439
Epoch: 5600 RMSE = 0.08866679470955477
Epoch: 5700 RMSE = 0.08609435036663259
Epoch: 5800 RMSE = 0.08370513001495336
Epoch: 5900 RMSE = 0.08149201675169497
Feature: [0. 1.], Label: [1.]
Output:  0.930091557523818
Feature: [1. 1.], Label: [0.]
Output:  0.06687678678385786
Feature: [1. 1.], Label: [0.]
Output:  0.06683575578228242
Feature: [1. 0.], Label: [1.]
Output:  0.9035794940105769
Feature: [0. 0.], Label: [0.]
Output:  0.09197314133811368
Feature: [0. 1.], Label: [1.]
Output:  0.9300858666494404
Feature: [1. 0.], Label: [1.]
Output:  0.9036776629149053
Feature: [0. 1.], Label: [1.]
Output:  0.9301480619669933
Feature: [0. 0.], Label: [0.]
Output:  0.0920231952633289
Feature: [0. 0.], Label: [0.]
Output:  0.09198304981563821
Feature: [1. 1.], Label: [0.]
Output:  0.06689491196740208
Feature: [1. 1.], Label: [0.]
Output:  0.06685385020166741
Feature: [0. 1.], Label: [1.]
Output:  0.9300900696171298
Feature: [1. 0.], Label: [1.]
Output:  0.9036475391792899
Feature: [0. 0.], Label: [0.]
Output:  0.09197589939139328
Feature: [1. 1.], Label: [0.]
Output:  0.0668772049810249
Epoch: 6000 RMSE = 0.07943584647890971
Epoch: 6100 RMSE = 0.07752063567358568
Epoch: 6200 RMSE = 0.07573035041836282
Epoch: 6300 RMSE = 0.0740481780114938
Epoch: 6400 RMSE = 0.07247051159730772
Epoch: 6500 RMSE = 0.07098823697261288
Epoch: 6600 RMSE = 0.06958021168134834
Epoch: 6700 RMSE = 0.06825274426852876
Epoch: 6800 RMSE = 0.0670011955974974
Epoch: 6900 RMSE = 0.06580708291467835
Feature: [0. 1.], Label: [1.]
Output:  0.942537642348875
Feature: [1. 1.], Label: [0.]
Output:  0.055015963473625536
Feature: [1. 1.], Label: [0.]
Output:  0.054991910215273714
Feature: [0. 1.], Label: [1.]
Output:  0.942527609674163
Feature: [1. 1.], Label: [0.]
Output:  0.054982392712979354
Feature: [0. 0.], Label: [0.]
Output:  0.07380974158717435
Feature: [0. 0.], Label: [0.]
Output:  0.07378818583811997
Feature: [0. 0.], Label: [0.]
Output:  0.07376664796531404
Feature: [0. 0.], Label: [0.]
Output:  0.07374512794465155
Feature: [0. 1.], Label: [1.]
Output:  0.942486708214325
Feature: [0. 1.], Label: [1.]
Output:  0.942504495982227
Feature: [1. 1.], Label: [0.]
Output:  0.05492541600654668
Feature: [1. 0.], Label: [1.]
Output:  0.921685149135516
Feature: [1. 1.], Label: [0.]
Output:  0.05494000234905637
Feature: [1. 0.], Label: [1.]
Output:  0.9217312069775395
Feature: [1. 0.], Label: [1.]
Output:  0.9218041604227677
Epoch: 7000 RMSE = 0.06466802595858301
Epoch: 7100 RMSE = 0.06358760181386701
Epoch: 7200 RMSE = 0.06256296172555167
Epoch: 7300 RMSE = 0.06158238425219125
Epoch: 7400 RMSE = 0.060643355569501886
Epoch: 7500 RMSE = 0.05974394555445038
Epoch: 7600 RMSE = 0.0588820753373237
Epoch: 7700 RMSE = 0.05805297539409482
Epoch: 7800 RMSE = 0.057259189783438864
Epoch: 7900 RMSE = 0.05649534769107487
Feature: [1. 1.], Label: [0.]
Output:  0.047661049077241634
Feature: [1. 1.], Label: [0.]
Output:  0.04764482014452585
Feature: [0. 0.], Label: [0.]
Output:  0.06317473069601405
Feature: [0. 0.], Label: [0.]
Output:  0.06316090194119942
Feature: [0. 1.], Label: [1.]
Output:  0.9501127300054016
Feature: [0. 1.], Label: [1.]
Output:  0.9501246754499388
Feature: [1. 0.], Label: [1.]
Output:  0.9327526724294887
Feature: [1. 1.], Label: [0.]
Output:  0.04765359223268948
Feature: [1. 0.], Label: [1.]
Output:  0.9327821579263276
Feature: [1. 0.], Label: [1.]
Output:  0.9328295335633
Feature: [0. 1.], Label: [1.]
Output:  0.9501616350679076
Feature: [0. 0.], Label: [0.]
Output:  0.06321847736708766
Feature: [0. 0.], Label: [0.]
Output:  0.06320462116026003
Feature: [0. 1.], Label: [1.]
Output:  0.950159081905289
Feature: [1. 1.], Label: [0.]
Output:  0.04768757742825196
Feature: [1. 1.], Label: [0.]
Output:  0.04767132349816812
Epoch: 8000 RMSE = 0.05575966294986155
Epoch: 8100 RMSE = 0.05505321926837632
Epoch: 8200 RMSE = 0.05436998927323032
Epoch: 8300 RMSE = 0.053710948029971395
Epoch: 8400 RMSE = 0.05307444269960097
Epoch: 8500 RMSE = 0.05246028061321603
Epoch: 8600 RMSE = 0.05186599058632366
Epoch: 8700 RMSE = 0.051290861697874134
Epoch: 8800 RMSE = 0.050734348238183256
Epoch: 8900 RMSE = 0.05019532309924682
Feature: [1. 1.], Label: [0.]
Output:  0.04257458380378115
Feature: [1. 0.], Label: [1.]
Output:  0.9402516638036355
Feature: [0. 0.], Label: [0.]
Output:  0.05604721914478418
Feature: [0. 1.], Label: [1.]
Output:  0.9553921523082888
Feature: [0. 1.], Label: [1.]
Output:  0.9554008832998455
Feature: [1. 1.], Label: [0.]
Output:  0.04258827851688403
Feature: [0. 1.], Label: [1.]
Output:  0.9554026991540355
Feature: [1. 0.], Label: [1.]
Output:  0.9402772180744862
Feature: [1. 0.], Label: [1.]
Output:  0.9403110578282351
Feature: [1. 1.], Label: [0.]
Output:  0.04262007544180272
Feature: [0. 0.], Label: [0.]
Output:  0.056068074848452366
Feature: [1. 1.], Label: [0.]
Output:  0.04260099840895491
Feature: [0. 0.], Label: [0.]
Output:  0.05605283858364446
Feature: [1. 1.], Label: [0.]
Output:  0.042581942992541706
Feature: [0. 1.], Label: [1.]
Output:  0.9553968013132796
Feature: [0. 0.], Label: [0.]
Output:  0.05604170987802187
Epoch: 9000 RMSE = 0.04967145286481632
Epoch: 9100 RMSE = 0.04916072690461705
Epoch: 9200 RMSE = 0.04866893290232672
Epoch: 9300 RMSE = 0.048188551591354
Epoch: 9400 RMSE = 0.047725489410410674
Epoch: 9500 RMSE = 0.047271281943876385
Epoch: 9600 RMSE = 0.046831381922750534
Epoch: 9700 RMSE = 0.046402532614272976
Epoch: 9800 RMSE = 0.04598408982706287
Epoch: 9900 RMSE = 0.04557789340132017
Feature: [1. 1.], Label: [0.]
Output:  0.038791544963610425
Feature: [0. 1.], Label: [1.]
Output:  0.9592892147352623
Feature: [0. 1.], Label: [1.]
Output:  0.9592959710639114
Feature: [0. 0.], Label: [0.]
Output:  0.050827665775018925
Feature: [1. 1.], Label: [0.]
Output:  0.038788181047889315
Feature: [1. 1.], Label: [0.]
Output:  0.03877896659678666
Feature: [1. 1.], Label: [0.]
Output:  0.038769758215766205
Feature: [0. 1.], Label: [1.]
Output:  0.9592827691461137
Feature: [0. 0.], Label: [0.]
Output:  0.05081106344753884
Feature: [0. 1.], Label: [1.]
Output:  0.9592856365185604
Feature: [1. 0.], Label: [1.]
Output:  0.9457028279219298
Feature: [0. 0.], Label: [0.]
Output:  0.05081785109372
Feature: [1. 1.], Label: [0.]
Output:  0.03877498786294855
Feature: [0. 0.], Label: [0.]
Output:  0.05080635374166729
Feature: [1. 0.], Label: [1.]
Output:  0.9456979638935743
Feature: [1. 0.], Label: [1.]
Output:  0.9457237614960552
Epoch: 10000 RMSE = 0.0451805142480962
Training finished.
 Final Training RMSE = 0.0451805142480962 

----- starting test
input_value: 0.0
input_value: 1.0
output_value: 0.9592980258208026
expected_value: 1.0
input_value: 1.0
input_value: 0.0
output_value: 0.9457495232745291
expected_value: 1.0
input_value: 0.0
input_value: 0.0
output_value: 0.05082107289449669
expected_value: 0.0
input_value: 1.0
input_value: 0.0
output_value: 0.9457495232745291
expected_value: 1.0
Final Testing RMSE = 0.050006000131158974

Process finished with exit code 0


"""