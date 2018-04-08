#!/bin/python

import sys
def currencies(n, s, m):
    # Complete this function
    fringe = []
    m,loopBest = loopFinder(n,s,m)
    node = [s,m,1,Counter()]
    best = 1
    while m:
        if node[1]==0:
            if node[2]> best:best = node[2]
        fringe+=getSuccessors(node)
        if len(fringe):node = fringe.pop(0)
        else:break
    best*=loopBest
    return best

def loopFinder(n, s, m):
    if m <40:return m,1
    global stateMax
    global levelMax
    global A
    fringe = []
    node = [s,40,1,Counter()]
    best = 0
    while 1:
        if node[1]==0:
            if node[2]> best:
                best = node[2]
                bestPath = node[3]
        fringe+=getSuccessors(node)
        if len(fringe):node = fringe.pop(0)
        else:break
    stateMax = [0.5]*n
    pathLength = len(bestPath)
    loop = 1
    loopLength = 0
    for x in bestPath:
        if bestPath[x]>3:
            loopLength +=1
            loop*= A[x[0]][x[1]]
    _m = m-pathLength-loopLength
    m = pathLength+loopLength + _m%loopLength
    loop = loops(loop,(_m//loopLength))
    loop = (loop*levelMax[m])%(7+10**9)
    return 0,loop

def loops(i,n):
    if n ==1:return (i%(7+10**9))
    A = n//2
    R = loops(i,A)%(7+10**9)
    if n%2:sol = (R*R*i)%(7+10**9)
    else: sol = (R*R)%(7+10**9)
    return sol

def getSuccessors(node):
    global A
    global f
    global stateMax
    global levelMax
    state,steps,multiplier,path = node
    successors = []
    if steps:
        if steps == 1:
            successors.append([state,steps-1,multiplier*A[state][f],path+Counter([(state,f)])])
        else:
            for i in xrange(len(A)):
                _mul = multiplier*A[state][i]
                if _mul > stateMax[i]:
                    successors.append([i,steps-1,_mul,path+Counter([(state,i)])])
                    stateMax[i]=_mul
                    if i==f:levelMax[41-steps]=_mul
    return successors

if __name__ == "__main__":
    from collections import Counter
    n = input()
    x, s, f, m = raw_input().strip().split(' ')
    x, s, f, m = [int(x), int(s), int(f), int(m)]
    A= []
    stateMax = [0.5]*n
    levelMax = [0]*41
    for A_i in xrange(n):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    print((x*currencies(n,s,m))%(7+10**9))
