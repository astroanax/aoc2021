#!/usr/bin/env python3

def main():
    with open('input') as input:
        print(part1(input))
    with open('input') as input:
        print(part2(input))

def part1(input):
    fishes = []
    for line in input:
        for x in line.strip().split(','):
            fishes.append(int(x))

    days =80
    for i in range(days):
        for j in range(len(fishes)):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
            else:
                fishes[j] -= 1
    return len(fishes)

def part2(input):
    fishes = []
    for line in input:
        for x in line.strip().split(','):
            fishes.append(int(x))

    days = 256

    for i in range(days):
        fishes = day(fishes) + fishes
    return len(fishes)

def day(fishes):
    newfishes = [0] * 9

    for i in range(len(fishes)):
        if i == 0:
            newfishes[6]+=fishes[0]
            newfishes[8]+=fishes[0]
        else:
            newfishes[i-1]+=fishes[i]
    return newfishes
if __name__=='__main__':
    main()
