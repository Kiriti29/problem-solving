"""
author: Muktevi Kiriti
"""

from binary_search_tree import BinarySearchTree


class PrintSnakeTree:

    def __init__(self):
        pass

    def print_snake_tree(self, bt):
        bst = BinarySearchTree(bt.pop(0))
        for i in bt:
            bst.add_node(i)
        print(bst.root)
        level = 1
        if level % 2 == 0:
            print_left_to_right(root, parent)
        else:
            print_right_to_left(root, parent)

    def print_left_to_right(self):
        pass

    def print_right_to_left(self):
        pass


if __name__ == "__main__":
    ps = PrintSnakeTree()
    print(ps.print_snake_tree([3, 1, 8, 6, 10, 7, 2]))


# if __name__ == "__main__":
#     bst = BinarySearchTree(3)
#     a = [1, 8, 6, 10, 7, 2]
#     for i in a:
#         bst.add_node(i)
#     print(bst.level)
