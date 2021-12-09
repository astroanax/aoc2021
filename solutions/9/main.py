#!/usr/bin/env python3

def check(i, j, grid, s):
    s+=1
    #print(grid[i][j][0], i, j)
    grid[i][j][1] = 1
    u=d=l=r=False
    b = 0
    if i == 0:
        u = True
    elif i == len(grid)-1:
        d = True
    if j == 0:
        l = True
    elif j == len(grid[0])-1:
        r = True
    
    if not u:
        if grid[i-1][j][0] == 9 or grid[i-1][j][1] == 1:
            u = True
    if not d:
        if grid[i+1][j][0] == 9 or grid[i+1][j][1] == 1:
            d = True
    if not l:
        if grid[i][j-1][0]==9 or grid[i][j-1][1] == 1:
            l = True
    if not r:
        if grid[i][j+1][0]==9 or grid[i][j+1][1] == 1:
            r = True

    if not u:
        if grid[i-1][j][1]!=1:
            s = check(i-1, j, grid, s)
    if not d:
        if grid[i+1][j][1]!=1:
            s = check(i+1, j, grid, s)
    if not l:
        if grid[i][j-1][1]!=1:
            s = check(i, j-1, grid, s)
    if not r:
        if grid[i][j+1][1]!=1:
            s = check(i, j+1, grid, s)

    print(grid[i][j][0], i, j)
    return s

with open('input') as input:
    lines = []
    for line in input:
        lines.append([ [int(x), 0] for x in line.strip()])

    ss = []
    sum = 0
    for i, line in enumerate(lines):
        for j, num  in enumerate(line):
            u=d=r=l=True
            if j!=0:
                if not num[0] < line[j-1][0]: l = False
            if j!=len(line)-1:
                if not num[0] < line[j+1][0]: r = False
            if i!=0:
                if not num[0] < lines[i-1][j][0]: u = False
            if i!=len(lines)-1:
                if not num[0]< lines[i+1][j][0]: u = False

            if u and d and l and r:
                sum+=1+num[0]
                ss.append(check(i,j,lines, 0))
                
            #print(num[0], end ='')
        print()

    for line in lines:
        for x in line:
            print(x[0], end= '')
        print()
    ss = sorted(ss)
    print(sum) 
    print(ss[-1]*ss[-2]*ss[-3])

