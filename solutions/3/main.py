#!/usr/bin/env python3

def main():
    with open('input') as lines:
        print(part2(lines))
        #print(part1(lines), part2(lines))

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
    numbers = []
    length = None
    for line in input:
        if length is None:
            length = len(line.strip())
        numbers.append(line.strip())

    numbers2 = numbers.copy()
    for i in range(length):
        for j in range(len(numbers)-1, -1, -1):
            num = numbers[j]
            if len(numbers) == 1:
                break
            pBit = 1 if (sum(int(n[i]) for n in numbers)/len(numbers)) >= 0.5 else 0
            if  not pBit == int(num[i]):
                numbers.remove(num)

    #print(numbers2)
    for i in range(length):
        pBit = None
        for j in range(len(numbers2)-1, -1, -1):
            num = numbers2[j]
            if len(numbers2) == 1:
                break
            if pBit is None:
                pBit = 1 if (sum(int(n[i]) for n in numbers2)/len(numbers2)) >= 0.5 else 0
            if  pBit == int(num[i]):
                numbers2.remove(num)

    return int('0b'+numbers[0], 2)*int('0b'+numbers2[0], 2)


if __name__=='__main__':
    main()
