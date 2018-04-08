#!/bin/python3

import os
import sys
from collections import Counter


# Complete the function below.

def maximumPermutation(w, s):
    # Return the string representing the answer.
    perms = Counter()
    i = len(w)
    val = sum(ord(x) ** 3 for x in w)
    y = s[:i]
    myval = sum(ord(x) ** 3 for x in y)
    _max = [0, '-1']

    if myval == val:
        perms[y] += 1

    for j in xrange(len(s) - i):
        myval -= ord(s[j]) ** 3
        myval += ord(s[i + j]) ** 3
        if myval == val:
            perms[s[j + 1:i + j + 1]] += 1

    for x in perms:
        if perms[x] < _max[0]:
            continue
        if _max[0] == perms[x]:
            _max[1] = min(_max[1], x)
        else:
            _max = [perms[x], x]

    return _max[1]


if __name__ == '__main__':
    t = input()
    for t_i in xrange(t):
        w = raw_input()
        s = raw_input()
        result = maximumPermutation(w, s)
        print result
