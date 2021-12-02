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

largerThanPrevDepth = 0
prevDepth = None
windowSums = [0] * (len(depths) -2 )

for i, depth in enumerate(depths):
    if prevDepth is None:
        windowSums[i//3] = windowSums[i//3] + depth
        prevDepth = depth
        continue
    # first group
    print('i is ', i, 'i//3 is', i//3, ' and adding ', windowSums[i//3], ' and ', depth)
    windowSums[i//3] = windowSums[i//3] + depth
    if i > 1:
        # second group
        print('i is ', i, ' and adding ', windowSums[(i//3)+1], ' and ', depth)
        windowSums[(i//3)+1] = windowSums[(i//3)+1] + depth
        if i > 2:
            # third group
            print('i is ', i, ' and adding ', windowSums[(i//3)+2], ' and ', depth)
            windowSums[(i//3)+2] = windowSums[(i//3)+2] + depth
    
largerThanPrevSum = 0
prevSum = None
for sum in windowSums:
    print(sum)
    if prevSum is None:
        prevSum = sum
        continue
    elif sum > prevSum:
        largerThanPrevSum = largerThanPrevSum + 1
    prevSum = sum

print(largerThanPrevSum)
