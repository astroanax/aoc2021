#!/usr/bin/env python3

with open('input') as input:
    lines = []
    for line in input:
        lines.append([[x, 0] for x in line.strip()])

    score = 0
    for l  in range(len(lines)-1, -1, -1):
        line = lines[l]
        first = True
        err = ''
        for i, c in enumerate(line):
            if err!='':
                lines.remove(line)
                break
            c = c[0]
            if c == '}' or c == ']' or c == ')' or c == '>':
                expected = ''
                if first:
                    prev = line[i-1][0]
                    if prev == '{':
                        expected = '}'
                    elif prev == '[':
                        expected = ']'
                    elif prev == '(':
                        expected = ')'
                    elif prev == '<':
                        expected = '>'
                    if c!=expected:
                        print('error, expected ', expected, ' found ', c, ' instead') 
                    else:
                        line[i-1][1] = line[i][1] = 1
                        first = False
                else:
                    if c == '}':
                        expected = '{'
                    elif c == ']':
                        expected = '['
                    elif c == ')':
                        expected = '('
                    elif c == '>':
                        expected = '<'
                    for j in range(i-1, 0, -1):
                        if line[j][1] == 1:
                            continue

                        if line[j][0]!=expected:
                            
                            err = line[j][0]
                            tmp = expected
                            expected = err
                            err = tmp

                            if err == '{':
                                err = '}'
                                score += 1197
                            elif err == '[':
                                err = ']'
                                score += 57
                            elif err == '(':
                                err = ')'
                                score += 3
                            elif err == '<':
                                err = '>'
                                score += 25137
                            if expected == '{':
                                expected = '}'
                            elif expected == '[':
                                expected = ']'
                            elif expected == '(':
                                expected = ')'
                            elif expected == '<':
                                expected = '>'
                            print('error, expected ', expected, ' found ', err, ' instead')
                            
                            break
                        else:
                            line[j][1] = line[i][1] = 1
                            break

    score2 = []
    for line in lines:
        y = 0
        for i in range(len(line)-1, -1, -1):
            if line[i][1]==1:
                line.remove(line[i])
            elif line[i][0] == '(':
                y = y*5 + 1
            elif line[i][0] == '{':
                y  = y*5 + 3
            elif line[i][0] == '[':
                y = y*5 + 2
            elif line[i][0] == '<':
                y = y*5 + 4
        score2.append(y)



    print(score, sorted(score2)[int(len(score2)/2)])
