def solve(hv,d):
    #gets total length left, up-down+right-left
    a = hv[0]-hv[1]+hv[3]-hv[2]
    #gets total diagonal left, upleft-downRight +upRight -downLeft
    a+= d[0]+d[1]-d[2]-d[3]
    return a

def dBlock(y,x,rQueen,cQueen):
    global queenD
    state = 2*(y<rQueen) + (x>cQueen)
    if state < 2 and y <= queenD[state]:
        queenD[state]=y-1
    elif state > 1 and y >= queenD[state]:
        queenD[state]=y+1
    
def hvBlock(obstacle,queen,pos):
    global queenHV
    if obstacle<queen and obstacle>=queenHV[pos[0]]:
        queenHV[pos[0]]=obstacle+1
    elif obstacle<=queenHV[pos[1]]:
        queenHV[pos[1]]=obstacle-1
        
n,k = map(int,raw_input().strip().split(' '))
rQueen,cQueen = map(int,raw_input().strip().split(' '))
queenHV= [n,1,1,n]#up,down,left,right
dUPL = rQueen+min(n-rQueen,cQueen-1)
dUPR = rQueen+min(n-rQueen,n-cQueen)
dDL = rQueen-min(rQueen-1,cQueen-1)
dDR = rQueen-min(rQueen-1,n-cQueen)
queenD= [dUPL,dUPR,dDL,dDR]#Diagonals...upLeft,upRight,downLeft,downRight
#print queenHV,queenD
for a0 in xrange(k):
    rObstacle,cObstacle = map(int,raw_input().strip().split(' '))
    if rObstacle==rQueen:
        hvBlock(cObstacle,cQueen,(2,3))
    elif cObstacle==cQueen:
        hvBlock(rObstacle,rQueen,(1,0))
    elif abs(rObstacle-rQueen) == abs(cObstacle-cQueen):
        dBlock(rObstacle,cObstacle,rQueen,cQueen)
#print queenHV,queenD
print solve(queenHV,queenD)
