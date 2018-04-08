def dfs(start,depth = 0):
    global arr
    global left
    depth+=1
    for x in arr[start]:
        if x in left:
            left.remove(x)
            depth = dfs(x,depth)
    return depth

q = int(raw_input().strip())
from collections import defaultdict
for a0 in xrange(q):
    n, m, x, y = raw_input().strip().split(' ')
    n, m, x, y = [int(n), int(m), long(x), long(y)]
    arr = defaultdict(set)
    for a1 in xrange(m):
        city_1, city_2 = raw_input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        arr[city_1].add(city_2)
        arr[city_2].add(city_1)
    if x < y or m == 0:print n*x
    else:
        total  = 0
        left = set(range(1,n+1))
        while len(left):
            start = left.pop()
            length = dfs(start)-1
            total+= x+length*y
        print total
