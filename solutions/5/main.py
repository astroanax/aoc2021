#!/usr/bin/env python3

def main():
    with open('input') as input:
        print(part1(input))
    with open('input') as input:
        print(part2(input))

def part1(input):
    pairs = []
    maxX = 0
    maxY = 0
    for line in input:
        segments = line.strip().split(' ')
        seg1 = segments[0].split(',')
        seg1 = [int(x) for x in seg1]
        seg2 = segments[-1].split(',')
        seg2 = [int(x) for x in seg2]
        if seg1[0] == seg2[0] or seg1[1] == seg2[1]:
            pairs.append([seg1,seg2])
            if maxX < seg1[0] or maxX < seg2[0]:
                maxX = seg1[0] if seg1[0] > seg2[0] else seg2[0]
            if maxY < seg1[1] or maxY < seg2[1]:
                maxY = seg1[1] if seg1[1] > seg2[1] else seg2[1]

    graph = []
    for i in range(0, maxY+1):
        graph.append([])
        for j in range(0, maxX+1):
            graph[i].append(0)
    
    for pair in pairs:
        if pair[0][0] == pair[1][0]:
            x = pair[0][0]
            y1 = min(pair[0][1], pair[1][1])
            y2 = max(pair[0][1], pair[1][1])
            for y in range(y1, y2+1):
                graph[y][x] += 1

        else:
            y = pair[0][1]
            x1 = min(pair[0][0], pair[1][0])
            x2 = max(pair[0][0], pair[1][0])
            for x in range(x1, x2+1):
                graph[y][x] += 1

    twos = 0
    for row in graph:
        for num in row:
            twos += 1 if num >=2 else 0
    return twos

def part2(input):
    pairs = []
    maxX = 0
    maxY = 0
    for line in input:
        segments = line.strip().split(' ')
        seg1 = segments[0].split(',')
        seg1 = [int(x) for x in seg1]
        seg2 = segments[-1].split(',')
        seg2 = [int(x) for x in seg2]
        pairs.append([seg1,seg2])
        if maxX < max(seg1[0], seg2[0]):
            maxX = max(seg1[0], seg2[0])
        if maxY < max(seg1[1], seg2[1]):
            maxY = max(seg1[1], seg2[1])

    graph = []
    for i in range(0, maxY+1):
        graph.append([])
        for j in range(0, maxX+1):
            graph[i].append(0)
    
    for pair in pairs:
        if pair[0][0] == pair[1][0]:
            x = pair[0][0]
            y1 = min(pair[0][1], pair[1][1])
            y2 = max(pair[0][1], pair[1][1])
            for y in range(y1, y2+1):
                graph[y][x] += 1

        elif pair[0][1] == pair[1][1]:
            y = pair[0][1]
            x1 = min(pair[0][0], pair[1][0])
            x2 = max(pair[0][0], pair[1][0])
            for x in range(x1, x2+1):
                graph[y][x] += 1

        else:
            x1 = pair[0][0]
            x2 = pair[1][0]
            y1 = pair[0][1]
            y2 = pair[1][1]

            xinc = range(x1, x2+1) if x2>x1 else range(x1, x2-1, -1)
            yinc = range(y1, y2+1) if y2>y1 else range(y1, y2-1, -1)
            for x, y in zip(xinc, yinc):
                graph[y][x] += 1

    twos = 0
    for row in graph:
        for num in row:
            twos += 1 if num >=2 else 0
    return twos

if __name__=='__main__':
    main()
