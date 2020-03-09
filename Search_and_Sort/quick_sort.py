"""
    author = Muktevi Kiriti
"""


class QuickSort:

    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    data = [7, 5, 1, 2, 6, 8, 4, 3]
    bs = QuickSort(data)
    print(bs.sort())
