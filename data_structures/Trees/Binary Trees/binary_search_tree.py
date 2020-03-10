"""
    author = Muktevi Kiriti
"""


class Node:

    def __init__(self):
        self.right = None
        self.left = None
        self.root = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = Node()

    def get_root(self):
        return self.root

    def get_parent(self, node):
        return node.parent

    def get_left_child(self, node):
        return node.left

    def get_right_child(self, node):
        return node.right

    def has_left_child(self, node):
        return node.left is not None

    def has_right_child(self, node):
        return node.right is not None

    def insert_node(self, value):
        root = self.root
        if root.root is None:
            root.root = value
            return
        while True:
            if value < root.root:
                if root.left:
                    root = root.left
                else:
                    new_node = Node()
                    new_node.root = value
                    new_node.parent = root
                    root.left = new_node
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    new_node = Node()
                    new_node.root = value
                    new_node.parent = root
                    root.right = new_node
                    break
        return

    def delete_node(self):
        pass


if __name__ == "__main__":
    bt = BinarySearchTree()
    test_input = [7, 5, 1, 2, 6, 8, 4]
    for i in test_input:
        bt.insert_node(i)
