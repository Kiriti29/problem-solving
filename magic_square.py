#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    r1 = s[0][0] + s[0][1] + s[0][2]
    r2 = s[1][0] + s[1][1] + s[1][2]
    r3 = s[2][0] + s[2][1] + s[2][2]
    c1 = s[0][0] + s[1][0] + s[2][0]
    c2 = s[0][1] + s[1][1] + s[2][1]
    c3 = s[0][2] + s[1][2] + s[2][2]
    d1 = s[0][0] + s[1][1] + s[2][2]
    d2 = s[0][2] + s[1][1] + s[2][0]
    print(r1, r2, r3, c1, c2, c3, d1, d2)


if __name__ == '__main__':

    ss = []
    # s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(ss)
