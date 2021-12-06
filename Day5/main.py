# from Utility.utility import fileReader
from pathlib import Path
import os
import sys
from collections import defaultdict


def part1(filename):
    dotMatrix = []
    edgeLength = 0
    fin = open(filename)
    readList = []
    for row in fin.readlines():
        temp_ = row.replace('\n', '').replace('\r', '')
        readList.append(temp_)
    processedList = list()
    for element in readList:
        pathList = []
        subElement = element.split(" -> ", 1)
        for item in subElement:
            path = item.split(",", 1)
            pathList.append((path[0], path[1]))
        processedList.append(pathList)

    vhList = []
    for row in processedList:
        for index, element in enumerate(row):
            if int(element[0]) > edgeLength:
                edgeLength = int(element[0])
            if int(element[1]) > edgeLength:
                edgeLength = int(element[1])
            if index == 0:
                if row[0][0] == row[1][0]:
                    vhList.append([row[0], row[1]])
                elif row[0][1] == row[1][1]:
                    vhList.append([row[0], row[1]])
    for i in range(edgeLength + 1):
        tempDot = []
        for j in range(edgeLength + 1):
            tempDot.append(0)
        dotMatrix.append(tempDot)

    for item in vhList:
        if item[0][0] == item[1][0]:
            if int(item[0][1]) < int(item[1][1]):
                for _ in range(int(item[0][1]), int(item[1][1]) + 1, 1):
                    dotMatrix[_][int(item[0][0])] += 1
            else:
                for _ in range(int(item[1][1]), int(item[0][1]) + 1, 1):
                    dotMatrix[_][int(item[0][0])] += 1
        if item[0][1] == item[1][1]:
            if int(item[0][0]) < int(item[1][0]):
                for _ in range(int(item[0][0]), int(item[1][0]) + 1, 1):
                    dotMatrix[int(item[0][1])][_] += 1
            else:
                for _ in range(int(item[1][0]), int(item[0][0]) + 1, 1):
                    dotMatrix[int(item[0][1])][_] += 1
    count2 = 0
    for k in dotMatrix:
        for _ in k:
            if _ >= 2:
                count2 += 1
    print(count2)


def day5(filename):
    infile = sys.argv[1] if len(sys.argv) > 1 else filename

    G1 = defaultdict(int)
    G2 = defaultdict(int)
    for line in open(infile):
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())
        dx = x2 - x1
        dy = y2 - y1

        for i in range(1 + max(abs(dx), abs(dy))):
            # x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0)) * i
            temp = 0
            if dx > 0:
                temp = 1
            else:
                if dx < 0:
                    temp = -1
                else:
                    temp = 0
            x = x1 + temp*i
            y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0)) * i
            if dx == 0 or dy == 0:
                G1[(x, y)] += 1
            G2[(x, y)] += 1
    print(len([k for k in G1 if G1[k] > 1]))
    print(len([k for k in G2 if G2[k] > 1]))


def part2(filename):
    dotMatrix = []
    edgeLength = 0
    fin = open(filename)
    readList = []
    for row in fin.readlines():
        temp_ = row.replace('\n', '').replace('\r', '')
        readList.append(temp_)
    processedList = list()
    for element in readList:
        pathList = []
        subElement = element.split(" -> ", 1)
        for item in subElement:
            path = item.split(",", 1)
            pathList.append((path[0], path[1]))
        processedList.append(pathList)
    vhList = []
    for i in processedList:
        for k, v in enumerate(i):
            # if k == 0:
            # if i[k][0] == i[k+1][0]
            print(k, v)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.in')
    test_input_file = Path(script_dir, '.', 'testInput.in')
    day5(test_input_file)
    # part2(test_input_file)
