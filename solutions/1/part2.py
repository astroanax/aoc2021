#!/usr/bin/env python3

depths = []

while True:
    try:
        line = input()
        try:
            if line:
                depths.append(int(line))
            else:
                break
        except:
            pass
    except:
        break

windowSums = [0] * (len(depths) - 2 )
for i, sum in enumerate(windowSums):
    windowSums[i] = depths[i] + depths[i+1] + depths[i+2]


largerThanPrevSum = 0
prevSum = None
for sum in windowSums:
    if prevSum is None:
        prevSum = sum
        continue
    elif sum > prevSum:
        largerThanPrevSum = largerThanPrevSum + 1
    prevSum = sum

print(largerThanPrevSum)
