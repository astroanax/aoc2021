#!/usr/bin/env python3

def main():
    with open('input') as lines:
        print(part2(lines))
        #print(part1(lines), part2(lines))

def part1(input):
    position = depth = 0
    for line in input:
        words = line.split() 
        if words[0][0]=='u':
            depth -= int(words[-1])
        elif words[0][0]=='d':
            depth += int(words[-1])
        elif words[0][0]=='f':
            position += int(words[-1])
    return position*depth

def part2(input):
    position = depth = aim = 0
    for line in input:
        words = line.split() 
        if words[0][0]=='u':
            aim -= int(words[-1])
        elif words[0][0]=='d':
            aim += int(words[-1])
        elif words[0][0]=='f':
            position += int(words[-1])
            depth += aim*int(words[-1])
    return position*depth

if __name__=='__main__':
    main()
