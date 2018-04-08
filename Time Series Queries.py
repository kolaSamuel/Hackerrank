#!/bin/python

import sys
from bisect import bisect_left
if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    t = map(int, raw_input().strip().split(' '))
    p = map(int, raw_input().strip().split(' '))
    _p,_t =[],[]
    pMax = 0
    tMax = 0
    for i in xrange(n):
        if p[i]>pMax:
            _p.append([p[i],i])
            pMax = p[i]
        tMax = max(tMax,p[n-i-1])
        _t.append([t[n-1-i],tMax])
    _t.sort()
    _p.sort()
    #print _t
    for a0 in xrange(q):
        _type, v = raw_input().strip().split(' ')
        _type, v = [int(_type), int(v)]
        if _type == 1:
            if v>pMax: print -1
            else:
                index = bisect_left(_p,[v,0])
                print t[_p[index][1]]
        else:
            if v>t[-1]:print -1
            else:
                index = bisect_left(_t,[v,0])
                #print 'found',v,index
                print _t[index][1]
