#!/usr/bin/env python3

import sys
def main():
    lines = []
    with open(sys.argv[1]) as input_lines:
        for line in input_lines:
            lines.append(line)

    print(part1(lines))
    print(part2(lines))

def part1(lines):
    nodes = {}

    for line in lines:
        n1, n2 = line.strip().split('-')
        if not n1 in nodes.keys():
            nodes[n1] = [n2]
        else:
            nodes[n1].append(n2)
        if not n2 in nodes.keys():
            nodes[n2] = [n1]
        else:
            nodes[n2].append(n1)
    
    return len([x for x in get_paths(nodes, ['start'])])

def get_paths(nodes, path):
    node = path[-1]
    if node == 'end':
        yield [*path, 'end']
    else:
        for edge in nodes[node]:
            if not edge == 'start':
                if not edge.islower() or edge not in path:
                    yield from get_paths(nodes, [*path, edge])

def part2(lines):
    nodes = {}

    for line in lines:
        n1, n2 = line.strip().split('-')
        if not n1 in nodes.keys():
            nodes[n1] = [n2]
        else:
            nodes[n1].append(n2)
        if not n2 in nodes.keys():
            nodes[n2] = [n1]
        else:
            nodes[n2].append(n1)
    
    return len([x for x in get_paths2(nodes, ['start'])])

def get_paths2(nodes, path):
    node = path[-1]
    if node == 'end':
        yield [*path, 'end']
    else:
        for edge in nodes[node]:
            if not edge == 'start':
                if not edge.islower() or edge not in path:
                    yield from get_paths2(nodes, [*path, edge])
                else:
                    smalls = {n: path.count(n) for n in path if n.islower()}
                    if not any(x>=2 for x in smalls.values()):
                        yield from get_paths2(nodes, [*path, edge])

#def get_path(nodes, node, path, seen):
#    valid_edge = 0
#    for edge in nodes[node]:
#        if not edge in seen and edge!='start' and edge!='end':
#            valid_edge+=1
#    if valid_edge == 0:
#        return path, []
#    path.append(node)
#    if node.islower():
#        seen.append(node)
#    print(node, seen, path)
#
#    for edge in nodes[node]:
#        if edge == 'start':
#            continue
#        #elif edge == 'end':
#        #    path.append('end')
#        #    global paths
#        #    paths.append(path)
#        #    path = []
#        #    return path, []
#        elif not edge in seen:
#            print(edge, node, seen, 'e', path)
#            path, seen = get_path(nodes, edge, path, seen)
#
#    return path, seen

#def get_path(nodes, node, path, seen):
#    path.append(node)
#    if node.islower():
#        seen.append(node)
#    if node == 'end':
#        return  path
#    print(nodes[node])
#    for edge in nodes[node]:
#        print(edge, seen, path, 0)
#        if edge == 'start' or edge in seen: continue
#        path = get_path(nodes, edge, path, seen)
#        print(edge, seen, path, 1)
#    return path


#def get_paths(nodes, node, seen):
#    seen.append(node)
#    print(seen, node, 0)
#    for edge in nodes[node]:
#        if edge == 'end':
#            seen.append('end')
#            continue
#        if edge == 'start':
#            continue
#        if edge not in seen:
#            seen = get_paths(nodes, edge, seen)
#    return seen

if __name__=='__main__':
    main()
