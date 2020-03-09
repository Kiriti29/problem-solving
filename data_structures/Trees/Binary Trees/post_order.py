"""
    author = Muktevi Kiriti
    logic - Left, Right, Root
"""

from Trees.binary_search_tree import BinarySearchTree


class PostOrder:

    def post_order(self, bt, parent):

        if bt.left:
            parent = bt
            self.post_order(bt.left, parent)
        if bt.right:
            self.post_order(bt.right, parent)
        print(bt.root)


if __name__ == "__main__":
    bt = BinarySearchTree()
    test_input = [7, 5, 1, 2, 6, 8, 4]
    for i in test_input:
        bt.insert_node(i)
    io = PostOrder()
    io.post_order(bt.get_root(), bt.get_root().parent)
