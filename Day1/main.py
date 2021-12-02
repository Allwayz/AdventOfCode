# Day 1: Sonar Sweep
from pathlib import Path
import os


def sonarSweep(filename):
    fin = open(filename)
    readList = fin.readlines()
    processedList = []
    result = 0
    tempValue = None
    for each in readList:
        newRow = each.replace('\n', '').replace('\r', '')
        processedList.append(int(newRow))
    for element in processedList:
        if tempValue is not None:
            if element > tempValue:
                result += 1
        tempValue = element
    print(result)


def sonarSweepThreeMeasurement(filename):
    fin = open(filename)
    processedList = []
    for each in fin.readlines():
        newRow = int(each.replace('\n', '').replace('\r', ''))
        processedList.append(newRow)

    threeMeasurementList = []
    for index, element in enumerate(processedList):
        if index + 3 == len(processedList):
            tempValue = processedList[index] + processedList[index + 1] + processedList[index + 2]
            threeMeasurementList.append(tempValue)
            break
        tempValue = processedList[index] + processedList[index + 1] + processedList[index + 2]
        threeMeasurementList.append(tempValue)

    value = None
    result = 0
    for element in threeMeasurementList:
        if value is not None:
            if element > value:
                result += 1
        value = element

    print(result)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.txt')
    # sonarSweep(input_file)
    sonarSweepThreeMeasurement(input_file)
