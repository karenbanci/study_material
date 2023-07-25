import numpy as np


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

    def __init__(self, features=None, labels=None, train_factor=0.9):
        """
        Will accept two lists-of-lists, one features and another one labels, and train_factor which defines
        how much of the data will be allocated to the training set.

        :param features: Be part of lists-of-list. Each row representing the features of one example from our data.
        :param labels: Be part of lists-of-lists. Each row representing one label from our data.
        :param train_factor: Represents the percentage of the data we want used as our training set.
        """
        self._features = None
        self._labels = None
        self._train_factor = NNData.percentage_limiter(train_factor)

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

    def load_data(self, features, labels):
        """
        Method that can be used to load or re-load data. This method was used by the constructor,
        but can also be called directly by the client. Besides that, creates numpy arrays from features and labels
        and assign them to self._features and self._labels. Validation to ensure that the provided data is
        consistent and of type float.
        """
        if features is None or labels is None:
            self._features = None
            self._labels = None
            return

        if len(features) != len(labels):
            self._features = None
            self._labels = None
            raise DataMismatchError
        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            raise ValueError


def load_XOR():
    """
    Spawns a new NNData object using these features and  labels. Sets a train factor of 1.
    """
    NNData(features=[[0, 0], [1, 0], [0, 1], [1, 1]],
           labels=[[0], [1], [1], [0]],
           train_factor=1)


load_XOR()


def unit_test():
    test_features_valid = [[0, 0], [1, 1]]
    test_labels_valid = [[0], [1]]
    features_array = np.array(test_features_valid)
    labels_array = np.array(test_labels_valid)
    empty_array = np.array([])
    test_labels_short = [[0]]
    test_labels_bad_data = [["a"], ["b"]]
    # Test constructor defaults
    print("Calling constructor with default arguments:", end="")
    my_data = NNData()
    if np.array_equal(my_data._features, empty_array) \
            and np.array_equal(my_data._labels, empty_array):
        print("PASS")
    else:
        print("FAIL")
    print("Calling constructor with valid arguments:", end="")
    my_data = NNData(test_features_valid, test_labels_valid)
    if np.array_equal(my_data._features, features_array) \
            and np.array_equal(my_data._labels, labels_array):
        print("PASS")
    else:
        print("FAIL")
    # Test mismatched constructor arguments
    print("Calling constructor with mismatched arguments:", end="")
    try:
        my_data = NNData(test_features_valid, test_labels_short)
        print("FAIL")
    except DataMismatchError:
        print("PASS")
    except:
        print("FAIL")
    # Test load_data with valid arguments
    print("Calling load_data() with valid arguments:", end="")
    my_data = NNData()
    my_data.load_data(test_features_valid, test_labels_valid)
    if np.array_equal(my_data._features, features_array) \
            and np.array_equal(my_data._labels, labels_array):
        print("PASS")
    else:
        print("FAIL")
    # Test load_data with mismatched arguments (start with a populated
    # dataset
    print("Calling load_data() with mismatched arguments:", end="")
    my_data = NNData(test_features_valid, test_labels_valid)
    try:
        my_data.load_data(test_features_valid, test_labels_short)
        print("FAIL")  # Execution should not reach this point
    except DataMismatchError:
        if my_data._features is None and my_data._labels is None:
            print("PASS")
        else:
            print("FAIL")
    # Test load_data with bad arguments (start with a populated
    # dataset
    print("Calling load_data() with bad arguments:", end="")
    my_data = NNData(test_features_valid, test_labels_valid)
    try:
        my_data.load_data(test_features_valid, test_labels_bad_data)
        print("FAIL")  # Execution should not reach this point
    except ValueError:
        if my_data._features is None and my_data._labels is None:
            print("PASS")
        else:
            print("FAIL")
    # Test percent limiter
    print("Testing train factor within bounds:", end="")
    my_data = NNData(test_features_valid, test_labels_valid, .5)
    if my_data._train_factor == .5:
        print("PASS")
    else:
        print("FAIL")
    print("Testing train factor too low:", end="")
    my_data = NNData(test_features_valid, test_labels_valid, -.1)
    if my_data._train_factor == 0:
        print("PASS")
    else:
        print("FAIL")
    print("Testing train factor within bounds:", end="")
    my_data = NNData(test_features_valid, test_labels_valid, 1.5)
    if my_data._train_factor == 1:
        print("PASS")
    else:
        print("FAIL")


unit_test()

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/Project CS_3B_Winter_2023/CS_3B_Winter_2023/ProjectNNData/NNData.py 

Calling constructor with default arguments:PASS
Calling constructor with valid arguments:PASS
Calling constructor with mismatched arguments:PASS
Calling load_data() with valid arguments:PASS
Calling load_data() with mismatched arguments:PASS
Calling load_data() with bad arguments:PASS
Testing train factor within bounds:PASS
Testing train factor too low:PASS
Testing train factor within bounds:PASS

Process finished with exit code 0
"""
