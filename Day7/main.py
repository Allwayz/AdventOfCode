# -*- coding: utf-8 -*-
# @Organization     : Cardiff School of Computer Science and Informatics
# @Project          : AdventOfCode
# @Author           : YuChen Liu
# @StudentNumber    : 21096441
# @Email            : LiuY282@cardiff.ac.uk
# @Time             : 07/12/2021 05:06
# @Function:
from pathlib import Path
import os
import sys


def day7(filename):
    infile = sys.argv[1] if len(sys.argv) > 1 else filename
    X = [int(x) for x in open(infile).read().strip().split(',')]
    res = []
    resSum = []
    for _ in range(min(X), max(X)+1):
        temp = 0
        tempSum = 0
        for i in X:
            temp += abs(i-_)
            n = abs(i-_)
            tempSum += (1+n) * (n/2)
        res.append(temp)
        resSum.append(tempSum)

    print("part1: ", min(res))
    print("part2: ", min(resSum))


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.in')
    test_input_file = Path(script_dir, '.', 'testInput.in')
    day7(input_file)
