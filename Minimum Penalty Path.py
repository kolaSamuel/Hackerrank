# Enter your code here. Read input from STDIN. Print output to STDOUT
def minPenalty(start,end,paths,travels,penalty=0,_min = 1024):
    global checks
    if start == end:
        return penalty
    for (x,y) in paths[start]:
        if travels[x]:continue
        dist = penalty|y
        if (x,dist) in checks:continue
        checks.add((x,dist))
        if _min > dist:
            travels[x]=True
            _min = min(_min,minPenalty(x,end,paths,travels,dist,_min))
            travels[x]=False
    return _min
checks = set()
n,m = map(int,raw_input().strip().split())
paths =[[] for _ in xrange(n+1)]
for _ in xrange(m):
    u,v,c = map(int,raw_input().strip().split())
    paths[u].append((v,c))
    paths[v].append((u,c))
start,end = map(int,raw_input().strip().split())
result = minPenalty(start,end,paths,[False]*(n+1))
print result
