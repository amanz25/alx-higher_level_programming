#!/usr/bin/python3
""" N Queens """

import sys


def check_position(b, h):
    """ check the position of the queen """
    for i in range(h):
        if b[h][1] is b[i][1]:
            return False
        if abs(b[h][1] - b[i][1]) == h - i:
            return False
    return True


def backtracking(b, h):
    """ backtrack the possibility """
    if h is N:
        print(b)
    else:
        for x in range(N):
            b[h][1] = x
            if check_position(b, h):
                backtracking(b, h + 1)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

b = [[h, 0] for h in range(N)]
backtracking(b, 0)
