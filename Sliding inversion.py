class fendwick(object):
    """Creates a binary index Tree"""
    def __init__(self,x,array):
        self.tree = array
        self.mn = float('inf')
        self.mx = x

    def getIndex(self,x,oper=1):
        """Gets the right index if oper = 1 and the left index if 0"""
        minimum = self.mn
        value=x
        index = 0
        #index = (self.tree[str(x)]-1) if oper else 0
        x = x if oper else x-1
        while x>=minimum:
            index+= self.tree[x]
            x = x-(x&(-x))
        if not index:self.mn = value
        return index

    def update(self,x,oper=1):
            """Adds to the tree if oper = 1 and removes if = -1"""
            maximum = self.mx
            self.tree[x]+=oper
            x = x+(x&(-x))
            while x <= maximum:
                self.tree[x]+=oper
                x = x+(x&(-x))
def positive(x):
    return int(x)+1+10**9
from collections import Counter
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(positive, raw_input().strip().split(' '))
vCount,count =0,0
slider = fendwick(1+2*10**9,Counter())
for i in xrange(m):
    count-=slider.getIndex(a[i])
    slider.update(a[i])
count+= (m-1)*m/2
vCount = count
length = m-1
for i in xrange(m,n):
    vCount-= slider.getIndex(a[i-m],0)
    slider.update(a[i-m],-1)
    vCount+= length-slider.getIndex(a[i])
    count+=vCount
    slider.update(a[i])
print count
