#!/usr/bin/env python3
import math

def main():
    #with open('input') as input:
        #print(part1(input))
    with open('input') as input:
        print(part2(input))

#def part1(input):
#    nums = {}
#    for line in input:
#        for n in line.strip().split(','):
#            if not int(n) in nums.keys():
#                nums[int(n)] = 1
#            else:
#                nums[int(n)] += 1
#    
#    meanPos = int(sum(nums[x]*x for x in nums)/sum(nums[x] for x in nums)/2)
#    sigmaDeviation = sum(nums[x]*math.fabs(meanPos-x) for x in nums)
#    return sigmaDeviation

def part1(input):
    nums = {}
    for line in input:
        for n in line.strip().split(','):
            if not int(n) in nums.keys():
                nums[int(n)] = 1
            else:
                nums[int(n)] += 1
                    
    maxPos = max(x for x in nums)
    distData = {}
    for i in range(maxPos):
        distData[i] = 0
        for x in nums:
            distData[i] += nums[x]*math.fabs(i-x)

    return min(distData[x] for x in distData)
def part2(input):
    nums = {}
    for line in input:
        for n in line.strip().split(','):
            if not int(n) in nums.keys():
                nums[int(n)] = 1
            else:
                nums[int(n)] += 1
                    
    meanPos = round(sum(x*nums[x] for x in nums)/sum(nums[x] for x in nums))
    #meanPos = (math.floor(meanPos)+math.ceil(meanPos))/2

    dist = 0
    for x in nums:
        d = math.fabs(meanPos-x)
        dist += nums[x]*(d*(d+1)/2)

    return dist

if __name__=='__main__':
    main()
