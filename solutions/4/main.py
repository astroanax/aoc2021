#!/usr/bin/env python3


def main():
    with open('input') as input:
        print(part2(input))

def part1(input):
    randNums = []
    boards = []
    boardNum = 0
    boardData = {}
    boardLength = None

    for line in input:
        if len(randNums) == 0:
            for num in line.strip().split(','):
                randNums.append(int(num))
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

            boards[boardNum].append([[int(num), 0] for num in line.split()])


    bingo = False
    bingoNum = 0
    bingoSum = 0
    for num in randNums:
        for board in boards:
            board = markNum(board, num)
            if checkBoard(board):
                print(num, 'lol')
                for row in board:
                    for num in board:
                        bingoSum += num[0] if not num[1] else 0
                bingo = True
                for row in board:
                    print(row)
                return bingoSum*num


def markNum(board, n):
    for row in board:
        for num in row:
            if num[0] == n:
                num[1] = 1

    return board

def checkBoard(board):
    for row in board:
        sum = 0
        for num in row:
            sum += num[1]
        if sum == len(row):
            return True
    
    for i in range(len(board[0])):
        sum = 0
        for row in board:
            sum += row[i][1]
        if sum == len(board[0]):
            return True

def part2(input):
    randNums = []
    boards = []
    boardNum = 0
    boardData = {}
    boardLength = None

    for line in input:
        if len(randNums) == 0:
            for num in line.strip().split(','):
                randNums.append(int(num))
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

            boards[boardNum].append([[int(num), 0] for num in line.split()])


    bingo = False
    bingoNum = 0
    bingoSum = 0
    for num in randNums:
        for i in range(len(boards)-1, -1, -1):
            board = boards[i]
            board = markNum(board, num)
            if checkBoard(board):
                if len(boards) != 1:
                    boards.remove(board)
                else:
                    print(num)
                    bingo = True
        if bingo:
            break

    sum =0
    for row in boards[0]:
        for num in row:
            sum += num[0] if num[1]==0 else 0
    print(sum)


if __name__=='__main__':
    main()
