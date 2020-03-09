from binary_search_tree import BinarySearchTree


class InOrder:

    def __init__(self):
        pass

    def in_order(self, root):
        parent = None
        while True:
            if root.left:
                parent = root
                root = root.left
                continue
            else:
                left_child = root.root
                root = parent
                print(left_child, parent.root)
                break

            # elif root.right:
            #     pass
            # else:
            #     break
