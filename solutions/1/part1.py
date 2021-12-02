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
for depth in depths:
    if prevDepth is None:
        prevDepth = depth
        continue
    elif depth > prevDepth:
        largerThanPrevDepth = largerThanPrevDepth + 1
    prevDepth = depth

print(largerThanPrevDepth)
