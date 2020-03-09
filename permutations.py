"""
author: kiriti
"""


class Permutations:

    def __init__(self):
        self.permutation = []

    def permutations(self, s):
        out = [x for x in s]
        self.permutation.append(out.pop())
        while len(out) != 0:
            self.join_str(out.pop())
        return self.permutation

    def join_str(self, s1):
        temp = []
        for i in range(0, len(self.permutation)):
            tmp1 = self.permutation.pop()
            for j in range(0, len(tmp1) + 1):
                temp.append(tmp1[:j] + s1 + tmp1[j:])
        self.permutation.extend(temp)


if __name__ == "__main__":
    p = Permutations()
    out = p.permutations("abcdef")
    print(out)
