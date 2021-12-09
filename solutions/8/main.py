#!/usr/bin/env python3

def main():
    with open('input') as input:
        print(part1(input))
    with open('input') as input:
        print(part2(input))

def part1(input):
    n =0
    for line in input:
        for signal in line[line.find('|')+1:].strip().split():
            if len(signal) == 2 or len(signal) == 4 or len(signal) == 3 or len(signal) == 7:
                n+=1

    return n

def part2(input):
    signals = {}
    segments = {}
    dSegments = {}

    for i, line in enumerate(input):
        segments[i] =[]
        dSegments[i] = []
        for segment in line[:line.find('|')].strip().split():
            segment = ''.join(sorted(segment))
            segments[i].append(segment)
            if len(segment) == 2:
                dSegments[i].append(1)
            elif len(segment) == 4:
                dSegments[i].append(4)
            elif len(segment) == 3:
                dSegments[i].append(7)
            elif len(segment) == 7:
                dSegments[i].append(8)
            else:
                dSegments[i].append(-1)

        signals[i] = []
        for signal in line[line.find('|')+1:].strip().split():
            signal = ''.join(sorted(signal))
            signals[i].append(signal)

    for i, line in enumerate(segments):
        fives = []
        sixes =[]
        for segment in segments[line]:
            if len(segment) == 5:
                fives.append(segment)
            if len(segment) == 6:
                sixes.append(segment)
        for s in segments[line]:
            if len(s) == 2:
                one = s
        for x in fives:
            if len(list(set(x) & set(one))) == 2:
                three = x
                
        dSegments[i][segments[line].index(three)] = 3
        fives.remove(three)
        six = ''
        for x in sixes:
            if len(list(set(x) & set(one))) == 1:
                six =x
        dSegments[i][segments[line].index(six)] = 6
        sixes.remove(six)
        for x in sixes:
            if len(list(set(x) & set(three))) == 4:
                zero = x
        dSegments[i][segments[line].index(zero)] = 0
        sixes.remove(zero)
        dSegments[i][segments[line].index(sixes[0])] = 9
        for x in fives:
            if len(list(set(x) & set(six))) == 5:
                five = x
        dSegments[i][segments[line].index(five)] = 5
        fives.remove(five)
        dSegments[i][segments[line].index(fives[0])] = 2

    print(dSegments)
    sum = 0
    print(signals)

    for i, line in enumerate(signals):
        print(i,  signals[i])
        n = ''
        for signal in signals[i]:
            n += str(dSegments[i][segments[i].index(signal)])
        sum += int(n)

        #signal = signals[i]
        #print(segments[i], dSegments[i])

    return sum

if __name__=='__main__':
    main()
