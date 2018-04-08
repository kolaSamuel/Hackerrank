# Enter your code here. Read input from STDIN. Print output to STDOUT
def bestPath(newLand,mLand,row,n,m):
    toAdd = 0
    for col in xrange(m):
        toAdd = max(toAdd+mLand[row][col],mLand[row][col])
        newLand[row][col] = toAdd
    toAdd = 0
    for col in xrange(m-2,-1,-1):
        toAdd = max(toAdd+mLand[row][col+1],0)
        newLand[row][col]+=toAdd

def update(newLand,mLand,updated,row,y,x=0,z=1):
    val = newLand[row][x]
    cost = newLand[row+1][x]
    for col in xrange(x,y,z):
        #print val,cost
        if val == newLand[row][col]:
            if val<0 and col != x:
                _cost = newLand[row+1][col]
                cost =  max(cost,_cost+val)
                updated[col-z] = cost+val
                cost = max(_cost,cost+val)
            else:
                cost = max(cost,newLand[row+1][col])
        elif val > newLand[row][col]:
            _cost,_val = newLand[row+1][col],newLand[row][col]
            if val <0:
                cost = max(cost,_val+_cost)
                updated[col-z]= cost+val
                _cost = max(_cost,cost+val)
            elif cost+val > _cost+_val:
                updated[col-z]= cost+val
                _cost = max(cost,_cost)
            cost,val = _cost,_val
        else:
            _cost,_val = newLand[row+1][col],newLand[row][col]
            if _val < 0:
                _cost = max(_cost,cost+val)
                updated[col-z]= max(cost,_cost+_val)+val
                cost,val = _cost,_val
            elif cost+val < _cost+_val:
                updated[col-z]= max(cost,_cost)+val
                cost,val = _cost,_val
            else:
                updated[col-z] = cost+val
                cost,val = max(_cost,cost+val-_val),_val
            
    updated[col]=cost+val
    #print z,updated,row
    x,y,z = y-z,x-z,z*-1
    fill(updated,x,y,z)  

def fill(updated,x,y,z):
    score = 0
    for col in xrange(x,y,z):
        if updated[col] != None:
            score = updated[col]
        updated[col] = score
    
def levelUp(newLand,mLand,row,n,m):
    update1 = [None]*m
    update2 = [None]*m
    update(newLand,mLand,update1,row,m)
    update(newLand,mLand,update2,row,-1,m-1,-1)
    for col in xrange(m):
        newLand[row][col]= max(update1[col],update2[col])
        
n,m = map(int,raw_input().strip().split())
mLand = [map(int,raw_input().strip().split()) for _ in xrange(n)]
newLand = [[0]*m for _ in xrange(n)]
for i in xrange(0,n):
    bestPath(newLand,mLand,i,n,m)
#for x in newLand:print x
#print
for row in xrange(n-2,-1,-1):
    levelUp(newLand,mLand,row,n,m)
#print
#for x in newLand:print x
print max(newLand[0])
