"""
    author = Muktevi Kiriti
    logic - Root, Left, Right
"""

from Trees.binary_search_tree import BinarySearchTree


class PreOrder:

    def pre_order(self, bt, parent):

        print(bt.root)
        if bt.left:
            parent = bt
            self.pre_order(bt.left, parent)
        if bt.right:
            self.pre_order(bt.right, parent)


if __name__ == "__main__":
    bt = BinarySearchTree()
    test_input = [7, 5, 1, 2, 6, 8, 4]
    for i in test_input:
        bt.insert_node(i)
    io = PreOrder()
    io.pre_order(bt.get_root(), bt.get_root().parent)
