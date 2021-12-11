#!/usr/bin/env python3

import sys
def main():
    lines = []
    with open(sys.argv[1]) as input_lines:
        for line in input_lines:
            lines.append(line)

    print(part1(lines))
    print(part2(lines))

flashes = 0
def part1(lines):
    grid = []
    for line in lines:
        grid.append([[int(x), False] for x in line.strip()])
    steps = int(sys.argv[2])
    for s in range(steps):
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                grid = increment(i, j, grid)
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                grid[i][j][1] = False
    return flashes

def part2(lines):
    grid = []
    for line in lines:
        grid.append([[int(x), False] for x in line.strip()])
    all_flash = None
    s = 0
    while True:
        s+=1
        sum = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                grid = increment(i, j, grid)
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                grid[i][j][1] = False
                sum+=grid[i][j][0]
        if sum == 0: return s
    

def increment(i,j, grid):
    if grid[i][j][0] > 8:
        grid[i][j][0] = 0
        grid[i][j][1] = True
        global flashes
        flashes+=1
        if i!=0:
            grid = increment(i-1, j, grid)
        if j!=0:
            grid = increment(i, j-1, grid)
        if i!=len(grid)-1:
            grid = increment(i+1, j, grid)
        if j!=len(grid[0])-1:
            grid = increment(i, j+1, grid)
        if i!=len(grid)-1 and j!=len(grid[0])-1:
            grid = increment(i+1, j+1, grid)
        if i!=0 and j!=0:
            grid = increment(i-1, j-1, grid)
        if i!=len(grid)-1 and j!=0:
            grid = increment(i+1, j-1, grid)
        if i!=0 and j!=len(grid[0])-1:
            grid = increment(i-1, j+1, grid)
    else:
        if grid[i][j][0] != 0 or not grid[i][j][1]:
            grid[i][j][0] += 1


    return grid

if __name__=='__main__':
    main()
