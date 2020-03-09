from node import Node


class BinaryTree:

    def __init__(self):
        pass

    def add_node(self, node):
        root = self.root
        while True:
            if root.left is None:
                root.left = Node(node)
            elif root.right is None:
                root.right = Node(node)
            elif root.left:
                root = root.left
