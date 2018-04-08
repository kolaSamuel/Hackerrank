n,q = map(int,raw_input().split(' '))
s = raw_input().strip()
arr = [list([0]*n) for _ in xrange(n)]
subStr = [[set(s[i]),s[i]] for i in xrange(n)]
for i in xrange(n):arr[i][i]= 1

for x in xrange(n-1,0,-1):
    i = n-x
    for y in xrange(x):
        subStr[y][1]+=s[y+i]
        subStr[y][0].update(subStr[y+1][0],[subStr[y][1]])
        arr[y][y+i] = len(subStr[y][0])
    if len(subStr[y][0])>=10**7:break
for a0 in xrange(q):
    left,right = raw_input().strip().split(' ')
    left,right = [int(left),int(right)]
    print arr[left][right]
