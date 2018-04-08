M,N,R = map(int,raw_input().split())
mat = [];MLR = []
for i in xrange(M):
    mat.append(raw_input().split())
    MLR.append(['0']*N)
lyrs = min(M,N)/2
for x in xrange(lyrs):
    dif = 1+2*x#to get sequence 1,3,5,7
    ar = R%(2*(M+N)-4*dif)
    lyr = []
    for i in xrange(x,M-1-x):lyr.append(mat[i][x])
    lyr += mat[M-1-x][x:N-x]
    for j in xrange(M-2-x,x,-1):lyr.append(mat[j][N-1-x])
    lyr += mat[x][N-x-1:x:-1]
    #print ar,lyr
    lyr = lyr[len(lyr)-ar:]+lyr[:len(lyr)-ar]
    #print 'turned',lyr
    for i in xrange(x,M-1-x):MLR[i][x]=lyr.pop(0)
    for j in xrange(x,N-x):MLR[M-1-x][j]=lyr.pop(0)
    for k in xrange(M-2-x,x,-1):MLR[k][N-1-x]=lyr.pop(0)
    for l in xrange(N-x-1,x,-1):MLR[x][l]=lyr.pop(0)
for x in MLR:print (" ".join(y for y in x))
