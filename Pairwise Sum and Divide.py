for _ in xrange(input()):
    N = input()
    A = map(int,raw_input().split())
    a2 = 0;ans = 0
    for i in xrange(N):
        if A[i]==1:ans+= N-1
        elif A[i]==2:a2+=1
    #print 'pre',ans
    if a2>1:
        y = a2-1
        ans+= (y+y**2)/2
    print ans#,a,a.values()
