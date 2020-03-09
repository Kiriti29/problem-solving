"""
    author = Muktevi Kiriti
"""

import math

from Search_and_Sort.bubble_sort import BubbleSort


class BinarySearch:

    def __init__(self, data):
        self.data = data

    def binary_search(self, start, end, value):

        data = self.data
        pivot = math.floor((start + end)/2)
        if value == data[pivot]:
            result = pivot
            return result
        if pivot == start or pivot == end:
            result = "Value not found"
            return result
        elif value > data[pivot]:
            start = pivot
            result = self.binary_search(start, end, value)
        elif value < data[pivot]:
            end = pivot
            result = self.binary_search(start, end, value)
        return result


if __name__ == "__main__":
    data = [7, 5, 1, 2, 6, 8, 4, 3, 100, 10]
    bs = BubbleSort(data)
    bs1 = BinarySearch(bs.sort())
    print(bs1.binary_search(0, len(data), 10))
