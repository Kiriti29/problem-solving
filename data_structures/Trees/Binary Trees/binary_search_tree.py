from node import Node


class BinarySearchTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def add_node(self, node):
        root = self.root
        while True:
            if node < root.root:
                if root.left is None:
                    root.left = Node(node)
                    break
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = Node(node)
                else:
                    root = root.right

    def delete_node(Self):
        pass
