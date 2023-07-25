import numpy as np
import random
from enum import Enum
import collections


class DataMismatchError(Exception):
    """
    NNData will enforce there must be exactly as many labels as features, and raise a DataMismatchError
    exception if the set sizes do not match.
    """
    pass


class NNData:
    """
    NNData will store data and deliver it in a way that is meaningful to the neural network.
    """

    class Set(Enum):
        TRAIN = 1
        TEST = 2

    class Order(Enum):
        RANDOM = 1
        SEQUENTIAL = 2

    def __init__(self, features=None, labels=None, train_factor=0.9):
        """
        Will accept two lists-of-lists, one features and another one labels, and train_factor which defines
        how much of the data will be allocated to the training set.

        :param features: Be part of lists-of-list. Each row representing the features of one example from our data.
        :param labels: Be part of lists-of-lists. Each row representing one label from our data.
        :param train_factor: Represents the percentage of the data we want used as our training set.
        :param train_indices: To point to the items in our dataset that make up the training set.
        :param test_indices: To point to the items in our dataset that make up the testing set.
        :param train_pool: To keep track of which training items have not yet been seen in a particular training epoch.
        :param test_pool: To keep track of which training items have not yet been seen in a testing run.
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
        This method avoids repeated code that will be used to empty data in load_data()
        """
        self._features = None
        self._labels = None

    def empty_data_and_split_set(self):
        """
        This method avoids repeated code that will be used to empty data in load_data()
        """
        self.empty_data()
        self.split_set()

    def load_data(self, features, labels):
        """
        Method that can be used to load or re-load data. This method was used by the constructor,
        but can also be called directly by the client. Besides that, creates numpy arrays from features and labels
        and assign them to self._features and self._labels. Validation to ensure that the provided data is
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
        This method will load one or both deques to be used as indirect indices.
        :param target_set: Will dictate whether we are loading self._train_pool.
        :param order: If order is NNData.Order.RANDOM, shuffle the pool(s) that you just created.
        If order is None or NNData.Order.SEQUENTIAL, leave the pool(s) in order.
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
        This method will deliver feature and label data for one example from either
        the training set or the testing set (client specifies which set is desired).
        """
        if target_set == NNData.Set.TRAIN or target_set is None:
            try:  # Return None if there are no indices left in the chose target_set.
                current_index = self._train_pool.popleft()
            except IndexError:
                return None

        else:  # Assuming target_set == NNData.Set.TEST:
            try:  # Return None if there are no indices left in the chose target_set.
                current_index = self._test_pool.popleft()
            except IndexError:
                return None

        current_feature = self._features[current_index]
        current_label = self._labels[current_index]
        current_tuple = (current_feature, current_label)
        return current_tuple

    def split_set(self, new_train_factor=None):
        """
        Shuffle all the examples and randomly assign them to the testing or training set, based on the training factor
        :param new_train_factor: It is the new value to train_factor.
        """
        if new_train_factor is not None:
            self._train_factor = NNData.percentage_limiter(new_train_factor)

        # Just do validation
        if self._features is None or self._labels is None:
            return

        number_of_examples = len(self._features)
        # Calculate and store the number of examples that should be used for training
        number_of_examples_for_training = number_of_examples * self._train_factor
        random_list = list(range(number_of_examples))
        random.shuffle(random_list)
        try:
            self._train_indices = random_list[:int(number_of_examples_for_training)]
            self._test_indices = random_list[int(number_of_examples_for_training):]
        except Exception as e:
            print(e)
        self.prime_data()

    def number_of_samples(self, target_set=None):
        """
        This method will return the number of examples in the testing set, the training set,
        or both combined (client specifies which set is desired).
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
        This method will return True when either the training set or testing set is exhausted
        (client specifies which set is desired).
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
    Spawns a new NNData object using these features and  labels. Sets a train factor of 1.
    """
    NNData(features=[[0, 0], [1, 0], [0, 1], [1, 1]],
           labels=[[0], [1], [1], [0]],
           train_factor=1)


load_XOR()


def unit_test():
    errors = False
    try:
        # Create a valid small and large dataset to be used later
        x = [[i] for i in range(10)]
        y = x
        our_data_0 = NNData(x, y)
        x = [[i] for i in range(100)]
        y = x
        our_big_data = NNData(x, y, .5)

        # Try loading lists of different sizes
        y = [[1]]
        try:
            our_bad_data = NNData()
            our_bad_data.load_data(x, y)
            raise Exception
        except DataMismatchError:
            pass
        except:
            raise Exception

        # Create a dataset that can be used to make sure the
        # features and labels are not confused
        x = [[1.0], [2.0], [3.0], [4.0]]
        y = [[.1], [.2], [.3], [.4]]
        our_data_1 = NNData(x, y, .5)

    except:
        print("There are errors that likely come from __init__ or a "
              "method called by __init__")
        errors = True

    # Test split_set to make sure the correct number of examples are in
    # each set, and that the indices do not overlap.
    try:
        our_data_0.split_set(.3)
        print(f"Train Indices:{our_data_0._train_indices}")
        print(f"Test Indices:{our_data_0._test_indices}")

        assert len(our_data_0._train_indices) == 3
        assert len(our_data_0._test_indices) == 7
        assert (list(set(our_data_0._train_indices +
                         our_data_0._test_indices))) == list(range(10))
    except:
        print("There are errors that likely come from split_set")
        errors = True

    # Make sure prime_data sets up the deques correctly, whether
    # sequential or random.
    try:
        assert our_data_0.number_of_samples(NNData.Set.TEST) == 7
        assert our_data_0.number_of_samples(NNData.Set.TRAIN) == 3
        assert our_data_0.number_of_samples() == 10
    except:
        print("Return value of number_of_samples does not match the "
              "expected value.")
    try:
        our_data_0.prime_data(order=NNData.Order.SEQUENTIAL)

        assert len(our_data_0._train_pool) == 3
        assert len(our_data_0._test_pool) == 7
        assert our_data_0._train_indices == list(our_data_0._train_pool)
        assert our_data_0._test_indices == list(our_data_0._test_pool)
        our_big_data.prime_data(order=NNData.Order.RANDOM)
        assert our_big_data._train_indices != list(our_big_data._train_pool)
        assert our_big_data._test_indices != list(our_big_data._test_pool)
    except:
        print("There are errors that likely come from prime_data")
        errors = True

    # Make sure get_one_item is returning the correct values, and
    # that pool_is_empty functions correctly.
    try:
        our_data_1.prime_data(order=NNData.Order.SEQUENTIAL)
        my_x_list = []
        my_y_list = []
        while not our_data_1.pool_is_empty():
            example = our_data_1.get_one_item()
            my_x_list.append(list(example[0]))
            my_y_list.append(list(example[1]))
        assert len(my_x_list) == 2
        assert my_x_list != my_y_list
        my_matched_x_list = [i[0] * 10 for i in my_y_list]
        assert my_matched_x_list == my_x_list
        while not our_data_1.pool_is_empty(our_data_1.Set.TEST):
            example = our_data_1.get_one_item(our_data_1.Set.TEST)
            my_x_list.append(list(example[0]))
            my_y_list.append(list(example[1]))
        assert my_x_list != my_y_list
        my_matched_x_list = [i[0] * 10 for i in my_y_list]
        assert my_matched_x_list == my_x_list
        assert set(i[0] for i in my_x_list) == set(i[0] for i in x)
        assert set(i[0] for i in my_y_list) == set(i[0] for i in y)
    except:
        print("There are errors that may come from prime_data, but could "
              "be from another method")
        errors = True

    # Summary
    if errors:
        print("You have one or more errors.  Please fix them before "
              "submitting")
    else:
        print("No errors were identified by the unit test.")
        print("You should still double check that your code meets spec.")
        print("You should also check that PyCharm does not identify any "
              "PEP-8 issues.")


unit_test()

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/Project CS_3B_Winter_2023/CS_3B_Winter_2023/ProjectNNData/NNData3.py 
Train Indices:[9, 3, 4]
Test Indices:[8, 5, 0, 2, 7, 6, 1]
No errors were identified by the unit test.
You should still double check that your code meets spec.
You should also check that PyCharm does not identify any PEP-8 issues.

Process finished with exit code 0
"""
