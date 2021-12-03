#!/usr/bin/env python3

def main():
    with open('input') as lines:
        print(part1(lines), part2(lines))

def part1(input):
    length = None
    numbers = []
    for line in input:
        if length is None:
            length = len(line.strip())
        numbers.append(line.strip())

    positionsData = [0] * length
    for number in numbers:
        for i in range(length):
            if int(number[i]) == 1:
                positionsData[i] += 1

    gamma = [0] * length
    for i in range(length):
        if positionsData[i] > len(numbers)/2:
            gamma[i] = 1

    gamma = ''.join(map(str, gamma))
    gamma = int('0b' + gamma, 2)
    epsilon = 2**length - 1 - gamma

    return gamma * epsilon
def part2(input):
    pass

if __name__=='__main__':
    main()
