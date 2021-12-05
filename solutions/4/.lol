#!/usr/bin/env python3

boardLength = None
boardData = {}
def main():
    with open('input') as input:
        print(part1(input))

def part1(input):
    randNums = []
    boards = []
    boardNum = 0
    global boardData
    global boardLength 

    for line in input:
        if len(randNums) == 0:
            randNums.append(int(num) for num in line.split(','))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                boardNum += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if boardNum == len(boards):
                boards.append([])

            boards[boardNum].append([int(num) for num in line.split()])
            print(boards[boardNum])

    for num in randNums:
        for i, board in enumerate(boards):
            markPos(board, num, i)

def markPos(board, num, boardNumber)
    foundPos =[]
    for i in range(boardLength):
        for j, row in enumerate(board):
            if row[i] == num:
                foundPos.append([i, j])

    if len(boardData[''.format(i)] == 0:
            boardData[''.format(i)] =[]
    boardData['{}'.format(i)].append = foundPos

def part2(input):
    for lines in input:
        pass

if __name__=='__main__':
    main()
