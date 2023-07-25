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
                x = 0
                for index, input_neurode in \
                        enumerate(self._layer_list.input_nodes):
                    input_neurode.set_input(features[index])
                    # print(f"{features[index]}")
                    x = features[index]

                for index, output_neurode in \
                        enumerate(self._layer_list.output_nodes):
                    output_value = output_neurode.value
                    error_value = labels[index] - output_value
                    sample_error += error_value ** 2
                    print(f"{x}-{output_value}")
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
    data = NNData(sin_X, sin_Y, 1)
    network.train(data, 10001, order=NNData.Order.SEQUENTIAL)
    data.split_set(0)
    network.test(data, order=NNData.Order.SEQUENTIAL)




print("\n\n--------------------------------------------------- Run Sin")
run_sin()
