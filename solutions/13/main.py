#!/usr/bin/env python3

import sys
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
    points = []
    foldsX = []
    foldsY = []
    first = None
    for line in lines:
        if ',' not in line:
            if 'y' not in line:
                if first is None:
                    first = 'x'
                foldsX.append(int(line[line.index('=')+1:]))
            else:
                if first is None:
                    first = 'y'
                foldsY.append(int(line[line.index('=')+1:]))
        else:
            points.append([int(x) for x in line.strip().split(',')])

    maxX = 0
    maxY = 0
    for point in points:
        if point[0]>maxX: maxX=point[0]
        if point[1]>maxY: maxY=point[1]

    graph = []
    for i in range(maxY+1):
        x = []
        for j in range(maxX+1):
            x.append(0)
        graph.append(x)

    for point in points:
        graph[point[1]][point[0]] = 1

    if first == 'y':
        for fold in foldsY:
            if fold < maxY/2:
                for i, row in enumerate(graph):
                    if i < fold+1 or i > 2*fold:
                        continue
                    else:
                        for j, n in enumerate(row):
                            if graph[i][j] == 1:
                                graph[2*fold - i][j]=1
                graph=graph[:fold]+graph[2*fold+1:]
            else:
                for i, row in enumerate(graph):
                    if i < fold+1:
                        continue
                    for j, n in enumerate(row):
                        if graph[i][j] == 1:
                            graph[2*fold - i][j]=1
                graph=graph[:fold]
            break

    else:
        for fold in foldsX:
            if fold < maxX/2:
                pass
            else:
                for i, row in enumerate(graph):
                    for j, n in enumerate(row):
                        if j < fold +1:
                            continue
                        if graph[i][j] == 1:
                            graph[i][2*fold-j] = 1
                    graph[i] = graph[i][:fold]
            break
            
    dots = 0
    for line in graph:
        dots += len([x for x in line if x == 1])
    return dots


def part2(lines):
    points = []
    folds = []
    for line in lines:
        if ',' not in line:
            if 'y' not in line:

                folds.append([int(line[line.index('=')+1:]), -1])
            else:
                folds.append([-1, int(line[line.index('=')+1:])])
        else:
            points.append([int(x) for x in line.strip().split(',')])

    maxX = 0
    maxY = 0
    for point in points:
        if point[0]>maxX: maxX=point[0]
        if point[1]>maxY: maxY=point[1]

    graph = []
    for i in range(maxY+1):
        x = []
        for j in range(maxX+1):
            x.append(0)
        graph.append(x)

    for point in points:
        graph[point[1]][point[0]] = 1

    for fold in folds:
        if fold[-1] != -1:
            fold = fold[-1]
            for i, row in enumerate(graph):
                if i < fold+1:
                    continue
                for j, n in enumerate(row):
                    if graph[i][j] == 1:
                        graph[2*fold - i][j]=1
            graph=graph[:fold]
        else:
            fold = fold[0]
            for i, row in enumerate(graph):
                for j, n in enumerate(row):
                    if j < fold +1:
                        continue
                    if graph[i][j] == 1:
                        graph[i][2*fold-j] = 1
                graph[i] = graph[i][:fold]
            
    dots = 0
    for line in graph:
        dots += len([x for x in line if x == 1])
        for x in line:
            if x == 1:
                print('#', end =' ')
            else:
                print(' ', end =' ')
        print()
    return dots

if __name__=='__main__':
    main()
