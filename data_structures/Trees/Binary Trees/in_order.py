"""
    author = Muktevi Kiriti
    logic - Left, Root, Right
"""

from Trees.binary_search_tree import BinarySearchTree


class InOrder:

    def in_order(self, bt, parent):

        if bt.left:
            parent = bt
            self.in_order(bt.left, parent)
        print(bt.root)
        if bt.right:
            self.in_order(bt.right, parent)


if __name__ == "__main__":
    bt = BinarySearchTree()
    test_input = [7, 5, 1, 2, 6, 8, 4]
    for i in test_input:
        bt.insert_node(i)
    io = InOrder()
    io.in_order(bt.get_root(), bt.get_root().parent)
