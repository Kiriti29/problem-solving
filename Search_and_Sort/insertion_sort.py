"""
    author = Muktevi Kiriti
"""


class InsertionSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        data = self.data
        for i in range(0, len(data)):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    tmp = data.pop(j)
                    data.insert(i, tmp)
        return data


if __name__ == "__main__":
    data = [7, 5, 1, 2, 6, 8, 10, 9, 100, 4, 3]
    bs = InsertionSort(data)
    print(bs.sort())