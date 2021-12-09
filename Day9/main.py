# -*- coding: utf-8 -*-
# @Project          : AdventOfCode
# @Author           : Allwayz
# @Time             : 09/12/2021 05:02
# @Function:
import itertools
from pathlib import Path
import os
import sys


def day9(filename):
    infile = sys.argv[1] if len(sys.argv) > 1 else filename
    X = []
    for _ in open(infile):
        X.append([int(x) for x in _.replace('\n', '')])
    # part 1
    sumList = []
    row = [-1, 0, 1, 0]
    col = [0, 1, 0, -1]
    # for _, __ in enumerate(X):
    #     for i, j in enumerate(__):
    #         if _ == 0:
    #             if i == 0:
    #                 if j < __[i + 1] and j < X[_ + 1][i]:
    #                     sumList.append(j)
    #             elif i == len(__) - 1:
    #                 if j < __[i - 1] and j < X[_ + 1][i]:
    #                     sumList.append(j)
    #             else:
    #                 if j < __[i + 1] and j < __[i - 1] and j < X[_ + 1][i]:
    #                     sumList.append(j)
    #         elif _ == len(X) - 1:
    #             if i == 0:
    #                 if j < X[_ - 1][i] and j < __[i + 1]:
    #                     sumList.append(j)
    #             elif i == len(__) - 1:
    #                 if j < X[_ - 1][i] and j < __[i - 1]:
    #                     sumList.append(j)
    #             else:
    #                 if j < __[i + 1] and j < __[i - 1] and j < X[_ - 1][i]:
    #                     sumList.append(j)
    #         else:
    #             if i == 0:
    #                 if j < __[i + 1] and j < X[_ + 1][i] and j < X[_ - 1][i]:
    #                     sumList.append(j)
    #             elif i == len(__) - 1:
    #                 if j < __[i - 1] and j < X[_ + 1][i] and j < X[_ - 1][i]:
    #                     sumList.append(j)
    #             else:
    #                 if j < X[_ + 1][i] and j < X[_ - 1][i] and j < __[i + 1] and j < __[i - 1]:
    #                     sumList.append(j)

    for _ in range(len(X)):
        for __ in range(len(X[0])):
            isGreater = False
            for i in range(len(row)):
                rowIndex = _ + row[i]
                colIndex = __ + col[i]
                if 0 <= rowIndex < len(X) and 0 <= colIndex < len(X[0]) and X[rowIndex][colIndex] <= X[_][__]:
                    isGreater = True
            if not isGreater:
                sumList.append(X[_][__])

    # part 2
    Sizes = []
    point = set()
    # Breadth-First
    for _ in range(len(X)):
        for __ in range(len(X[0])):
            if not {(_, __)}.issubset(point) and X[_][__] != 9:
                size = 0
                Q = [(_, __)]
                while Q:
                    (_, __) = Q.pop()
                    if (_, __) in point:
                        continue
                    point.add((_, __))
                    size += 1
                    for i in range(4):
                        rowIndex = _ + row[i]
                        colIndex = __ + col[i]
                        if 0 <= rowIndex < len(X) and 0 <= colIndex < len(X[0]) and X[rowIndex][colIndex] != 9:
                            Q.append((rowIndex, colIndex))
                Sizes.append(size)
    Sizes.sort()

    print("part1: ", sum(sumList) + len(sumList))
    print("part2: ", Sizes[-1] * Sizes[-2] * Sizes[-3])


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.in')
    test_input_file = Path(script_dir, '.', 'testInput.in')
    day9(input_file)
