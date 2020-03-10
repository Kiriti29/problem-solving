"""
author: Muktevi Kiriti
"""

from binary_search_tree import BinarySearchTree


class PrintSnakeTree:

    def __init__(self):
        pass

    def print_snake_tree(self, bt):
        bst = BinarySearchTree()
        for i in bt:
            bst.insert_node(i)
        print(bst.root.root)
        level = 1
        tmp = [bst.root]
        while tmp:
            if level % 2 != 0:
                tmp = self.print_left_to_right(bst, tmp)
            else:
                tmp = self.print_right_to_left(bst, tmp)
            level += 1

    def print_left_to_right(self, bst, tmp):
        temp = []
        for i in tmp:
            left = bst.get_left_child(i)
            right = bst.get_right_child(i)
            if left:
                print(left.root)
            if right:
                print(right.root)
                temp.append(right)
            if left:
                temp.append(left)
        return temp

    def print_right_to_left(self, bst, tmp):
        temp = []
        for i in tmp:
            left = bst.get_left_child(i)
            right = bst.get_right_child(i)
            if right:
                print(right.root)
            if left:
                print(left.root)
                temp.append(left)
            if right:
                temp.append(right)
        return temp


if __name__ == "__main__":
    ps = PrintSnakeTree()
    print(ps.print_snake_tree([3, 1, 8, 6, 10, 7, 2]))


# if __name__ == "__main__":
#     bst = BinarySearchTree(3)
#     a = [1, 8, 6, 10, 7, 2]
#     for i in a:
#         bst.add_node(i)
#     print(bst.level)
