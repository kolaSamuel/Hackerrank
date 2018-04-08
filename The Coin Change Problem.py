#!/bin/python
from bisect import bisect_right
def getWays(n, c):
    # Complete this function
    size = len(c)
    sizeLimit = 2**24
    fringe = [(i,x) for (i,x) in enumerate(c)]
    ways = 1 if any(x==n for x in c) else 0
    count = 0
    while count < len(fringe):
        pointer,change = fringe[count]
        for i in xrange(pointer,size):
            _newChange = c[i]+change
            if _newChange == n:ways+=1
            elif _newChange+c[i]== n:ways+=1
            elif _newChange+c[i] < n:fringe.append((i,_newChange))
            else:break
        count+=1
        if len(fringe) > sizeLimit:
            #print ways,' ways so far'
            #print count,len(fringe)
            fringe = fringe[count:]
            count = 0
    return ways

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(int, raw_input().strip().split(' '))
c.sort()
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c[:bisect_right(c,n)])
print ways
