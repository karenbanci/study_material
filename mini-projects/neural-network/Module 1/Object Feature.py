class exampleclass:

    def __init__(self, features = None, labels = None):
        self._features = None
        self._labels = None
        if features is None:
            features = []
        if labels is None:
            labels = []
        self.load_data(features, labels)

    def load_data(self, features = None, labels = None):
        print(features)

my_object = exampleclass([1,2,3], [4,5,6])