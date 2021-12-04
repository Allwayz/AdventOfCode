from Utility.utility import fileReader
from pathlib import Path
import os


def bingo(filename):
    inputList = fileReader(filename)
    randomOrder = []
    randomBoards = []
    tempBorder = []
    for index, line in enumerate(inputList):
        if index == 0:
            tempList = line.split(',')
            for subItem in tempList:
                randomOrder.append(subItem)
        else:
            if len(line) == 0 and index != 1:
                randomBoards.append(tempBorder)
                tempBorder = []
            elif len(inputList) == index + 1:
                tempBorderList = line.split()
                tempBorder.append(tempBorderList)
                randomBoards.append(tempBorder)
                tempBorder = []
            elif index != 1:
                tempBorderList = line.split()
                tempBorder.append(tempBorderList)

    print(randomBoards)

    def checkWin(boards):
        for boardIndex, board in enumerate(boards):
            for i in range(0, len(board[0])):
                if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == 'X':
                    return board
                if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == 'X':
                    return board

    def getWinner(order, boards):
        resultHit = 0
        isWin = 0
        ids = 8
        for hits in order:
            for i, Board in enumerate(boards):
                for j, lines in enumerate(Board):
                    for index, item in enumerate(lines):
                        if item == hits:
                            lines[index] = 'X'
                        if checkWin(boards) is not None:
                            isWin = 1
                            resultHit = hits
                            ids = i
            if isWin == 1:
                print(resultHit, ids)
                break
        return [boards[ids], resultHit]

    # winList = getWinner(randomOrder, randomBoards)
    # print(winList[0])
    # resultCount = 0
    # for line in winList[0]:
    #     for k in line:
    #         if k != 'X':
    #             resultCount += int(k)
    # print(resultCount * int(winList[1]))


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = Path(script_dir, '.', 'puzzleInput.in')
    test_input_file = Path(script_dir, '.', 'testInput.txt')
    bingo(input_file)
