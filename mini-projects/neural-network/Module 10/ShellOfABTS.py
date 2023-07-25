class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    class NotFoundError(Exception):
        pass

    class EmptyTreeError(Exception):
        pass

    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def find(self, key):
        return self._find(key, self._root)

    def _find(self, key, sub_root):
        if sub_root is None:
            raise BinarySearchTree.NotFoundError
        if key < sub_root.data:
            return self._find(key, sub_root.left_child)
        if sub_root.data < key:
            return self._find(key, sub_root.right_child)
        else:
            return sub_root.data
