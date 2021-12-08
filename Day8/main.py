# -*- coding: utf-8 -*-
# @Project          : AdventOfCode
# @Author           : Allwayz
# @Time             : 07/12/2021 05:32
# @Function:
import itertools
from pathlib import Path
import os
import sys


def day8(filename):
    Digits = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: ''
    }
    infile = sys.argv[1] if len(sys.argv) > 1 else filename
    X = []
    count = 0
    for x in open(infile).readlines():
        _ = x.replace('\n', '').replace('\r', '').split('|')
        before = _[0].split()
        after = _[1].split()
        X.append([before, after])
        for element in after:
            if len(element) == 2 or len(element) == 4 or len(element) == 3 or len(element) == 7:
                count += 1
    sum = 0
    for i in X:
        for j in i[0]:
            if len(j) == 7:
                Digits[8] = set(j)
            elif len(j) == 2:
                Digits[1] = set(j)
            elif len(j) == 3:
                Digits[7] = set(j)
            elif len(j) == 4:
                Digits[4] = set(j)
    # for i in X:
        for j in i[0]:
            if len(j) != 2 and len(j) != 4 and len(j) != 3 and len(j) != 7:
                if len(j) == 6:
                    if not Digits[1].issubset(set(j)):
                        Digits[6] = set(j)
                    elif not Digits[4].issubset(set(j)):
                        Digits[0] = set(j)
                    else:
                        Digits[9] = set(j)
                elif len(j) == 5:
                    if Digits[1].issubset(set(j)):
                        Digits[3] = set(j)
                    elif Digits[8].issubset(Digits[4].union(set(j))):
                        Digits[2] = set(j)
                    else:
                        Digits[5] = set(j)
        # print(Digits)
        digitList = [0, 0, 0, 0]
        for index, _ in enumerate(i[1]):
            digitSet = set(_)
            for k, v in Digits.items():
                # print(len(digitSet.difference(set(v))) == 0,set(v),digitSet)
                if digitSet.issubset(set(v)) and digitSet.issuperset(set(v)):
                    # print(k)
                    digitList[index] = k
        i.append(digitList)
        # print(Digits)
    for i in X:
        sum += int(''.join(str(e) for e in i[2]))

    print("part1: ", count)
    print("part2: ", sum)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.in')
    test_input_file = Path(script_dir, '.', 'testInput.in')
    day8(input_file)
