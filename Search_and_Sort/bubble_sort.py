"""
    author = Muktevi Kiriti
"""


class BubbleSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(0, len(self.data)):
            for j in range(0, i):
                if self.data[j] > self.data[i]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
        return self.data


if __name__ == "__main__":
    data = [7, 5, 1, 2, 6, 8, 4, 3]
    bs = BubbleSort(data)
    print(bs.sort())
