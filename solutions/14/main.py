#!/usr/bin/env python3

import sys
from collections import defaultdict
def main():
    lines = []
    with open(sys.argv[1]) as input_lines:
        for line in input_lines:
            if len(line.strip()) == 0:
                continue
            lines.append(line)
    #print(part1(lines))
    print(part2(lines))

def part1(lines):
    template = lines[0].strip()
    lines = lines[1:]
    rules = []
    for line in lines:
        x = line.strip().split('->')
        rules.append([x[0].strip(), x[1].strip()])

    for i in range(int(sys.argv[2])):
        for rule in rules:
            if rule[0] in template:
                while template.count(rule[0]) > 0:
                    template = template.replace(rule[0],rule[0][0]+'.'+rule[1]+'.'+rule[0][1])
        template = template.replace('.', '')

    return template.count(most_common(template)) - template.count(least_common(template))


def part2(lines):
    template = lines[0].strip()
    lines = lines[1:]
    rules = {}

    for line in lines:
        x = line.strip().split('->')
        rules[x[0].strip()]=x[1].strip()

    polymer = defaultdict(int)
    for x in zip(template, template[1:]):
            polymer[str(x[0]+x[1])] += 1


    for i in range(int(sys.argv[2])):
        old_polymer = polymer.copy()
        for rule in rules:
            if rule not in old_polymer:
                continue
            polymer[rule[0]+rules[rule]] += old_polymer[rule]
            polymer[rules[rule]+rule[1]] += old_polymer[rule]
            polymer[rule] -= old_polymer[rule]
        #for p, c in list(polymer.items()):
        #    if not p in rules:
        #        continue
        #    polymer[p[0]+rules[p]] += c
        #    polymer[rules[p]+p[1]] += c
        #    polymer[p] -= c

    counts = defaultdict(int)
    for j in polymer:
        counts[j[0]]+=polymer[j]

    counts[template[-1]]+=1
    print(max(counts.values()) - min(counts.values()))
#def part2(lines):
#    template = lines[0].strip()
#    lines = lines[1:]
#    rules = {}
#    for line in lines:
#        x = line.strip().split('->')
#        rules[x[0].strip()]=x[1].strip()
#
#    polymer = {str(x[0]+x[1]) :1 for x in zip(template, template[1:])}
#    print(polymer, rules)
#    new_polymer = {}
#    for i in range(int(sys.argv[2])):
#        print(polymer)
#        for rule in rules:
#            if rule in polymer:
#                if polymer[rule] > 0:
#                    if not rule[0]+rules[rule] in new_polymer:
#                        new_polymer[rule[0]+rules[rule]]=polymer[rule]
#                    else:
#                        new_polymer[rule[0]+rules[rule]]+=polymer[rule]
#                    if not rules[rule]+rule[1] in new_polymer:
#                        new_polymer[rules[rule]+rule[1]]=polymer[rule]
#                    else:
#                        new_polymer[rules[rule]+rule[1]]+=polymer[rule]
#                    polymer[rule] = 0
#        for x in polymer:
#            if x in new_polymer:
#                polymer[x]+=new_polymer.pop(x)
#        y=set(new_polymer.keys())
#        for x in y:
#            polymer[x] = new_polymer.pop(x)
#        new_polymer={}
#    print(polymer)
#    count={}
#    for x in polymer:
#        if x[0] not in count.keys():
#            count[x[0]] = polymer[x]
#        else:
#            count[x[0]] += polymer[x]
#        #if x[1] not in count.keys():
#        #    count[x[1]] = polymer[x]
#        #else:
#        #    count[x[1]] += polymer[x]
#
#    max_c = None
#    min_c = None
#    for x in count:
#        if max_c is None: max_c = x
#        elif count[x] > count[max_c]: max_c = x
#        if min_c is None: min_c = x
#        elif count[x] < count[min_c]: min_c = x
#    print(max_c, min_c, count[max_c]+1-count[min_c])

#def part2(lines):
#    t = lines[0].strip()
#    polymer = {}
#    for i, x in enumerate(t):
#        if i == len(t)-1: continue
#        if x+t[i+1] not in polymer.keys():
#            polymer[x+t[i+1]] = 1
#        else:
#            polymer[x+t[i+1]] += 1
#
#    lines = lines[1:]
#    rules = {}
#    for line in lines:
#        x = line.strip().split('->')
#        rules[x[0].strip()]=x[1].strip()
#
#    for i in range(int(sys.argv[2])):
#        for rule in rules:
#            if rule in polymer.keys():
#                if polymer[rule] > 0:
#                    polymer[rule] -= 1
#                    if not rule[0] + rules[rule].lower() in polymer.keys():
#                        polymer[rule[0] + rules[rule].lower()] = 1
#                    else:
#                        polymer[rule[0] + rules[rule].lower()] += 1
#                    if not rules[rule].lower() + rule[1] in polymer.keys():
#                        polymer[rules[rule].lower() + rule[1]] = 1
#                    else:
#                        polymer[rules[rule].lower() + rule[1]] += 1
#        y = set(polymer.keys())
#        for x in y:
#            if not x.isupper():
#                if not x.upper() in polymer.keys():
#                    polymer[x.upper()] = polymer.pop(x)
#                else:
#                    polymer[x.upper()] += polymer.pop(x)
#
#
#    print(polymer)
#    count={}
#    for x in polymer:
#        if x[0] not in count.keys():
#            count[x[0]] = 1
#        else:
#            count[x[0]] += 1
#        if x[1] not in count.keys():
#            count[x[1]] = 1
#        else:
#            count[x[1]] += 1
#
#    max_c = None
#    for x in count:
#        if max_c is None: max_c = x
#        elif count[x] > count[max_c]: max_c = x
#
#    print(max_c, count[max_c])

def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

if __name__=='__main__':
    main()
