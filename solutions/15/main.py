#!/usr/bin/env python3

import sys
from collections import defaultdict
from math import inf as infinity
import heapq
def main():
    lines = []
    with open(sys.argv[1]) as input_lines:
        for line in input_lines:
            if len(line.strip()) == 0:
                continue
            lines.append(line)
    print(part1(lines))
    print(part2(lines))

def part1(lines):
    grid = []
    for line in lines:
        grid.append([int(x) for x in line.strip()])
    path = reversed(dijkstra(grid, (0,0)))
    risk = 0
    for x, y in path:
        risk+=grid[x][y]
    
    return risk-grid[0][0]

def dijkstra(grid, source):
    dist = {}
    prev = {}
    queue = []

    for m, line in enumerate(grid):
        for n, x in enumerate(line):
                dist[(m, n)] = infinity
                prev[(m, n)] = None
    #            queue.append((m, n))
    dist[source] = 0
    heapq.heappush(queue, (0, source))

    while len(queue)!=0:
        u = heapq.heappop(queue)

        x, y = u[1]
        #if x == len(grid)-1 and y == len(grid[0])-1:
        #    break

        for i, j in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                continue
            v = (i, j)
            #if not v in queue: continue
            alt = dist[u[1]] + grid[x][y]
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(queue, (dist[v], v))
                prev[v] = u[1]
    path = []
    u = (len(grid)-1,len(grid[0])-1)
    if prev[u] is not None or u == source:
        while u is not None:
            path.append(u)
            u = prev[u]
    return path

#def part1(lines):
#    grid = []
#    for line in lines:
#        grid.append([int(x) for x in line.strip()])
#
#    neighbir
#def lowest_risk(grid, i, j):
#    path = pathfind(grid, [[i,j]])
#    risk = 0
#    for i, j in path:
#        risk+=grid[i][j]
#    return risk
#
#def pathfind(grid, path):
#    [i, j] = path[-1]
#    print(grid[i][j])
#    if path[-1] == [len(grid)-1, len(grid[0])-1]:
#        return path,risk
#    else:
#        if i!=len(grid)-1:
#            if j!=len(grid[0])-1:
#                if grid[i+1][j]>grid[i][j+1]:
#                    path.append([i,j+1])
#                    return pathfind(grid, path)
#                else:
#                    path.append([i+1,j])
#                    return pathfind(grid, path)
#            else:
#                path.append([i+1,j])
#                return pathfind(grid, path)
#        else:
#            path.append([i,j+1])
#            return pathfind(grid, path)

def part2(lines):
    grid = []
    for line in lines:
        full_line = []
        for i in range(5):
            full_line+=[int(x)+i if int(x)+i<10 else (int(x)+i)%9 for x in line.strip() ]
        grid.append(full_line)

    new_grid=[]
    for i in range(4):
        tmp = []
        for line in grid:
            tmp.append([x+i+1 if x+i+1<10 else (x+i+1)%9 for x in line])
        new_grid+=tmp
    grid+=new_grid

    path = reversed(dijkstra(grid, (0,0)))
    risk = 0
    for x, y in path:
        risk+=grid[x][y]
    
    return risk-grid[0][0]


if __name__=='__main__':
    main()
