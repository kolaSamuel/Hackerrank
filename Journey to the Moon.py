# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys
sys.setrecursionlimit(1500)
class graphTree(object):
    def __init__(self,x):
        self.total = x
        self.graph = defaultdict(set)
        self.left = x
        self.nodes = set()
        self.firstGen = []
    
    def add(self,a,b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.graph[a].add(b)
        self.graph[b].add(a)
        
    def solve(self):
        """ helper function to depths"""
        self.left -= len(self.nodes)
        
        def depths(x,depth = 0):
            depth+=1
            for y in self.graph[x]:
                if y in self.nodes:
                    self.nodes.remove(y)
                    depth = depths(y,depth)
            return depth
        
        while len(self.nodes):
            x = self.nodes.pop()
            self.firstGen.append(depths(x))
        #print self.graph
        #print self.nodes
        #print self.firstGen
    
    def __str__(self):
        lefts = self.left
        tots = self.total
        answer = (lefts*(lefts-1))/2
        l = len(self.firstGen)
        for i in xrange(l):
            x = self.firstGen[i]
            tots-=x
            answer+= x*(tots)
        return str(answer)
    
N,l = map(int,raw_input().split())
tree = graphTree(N)
for i in xrange(l):
    a,b = map(int,raw_input().split())
    # Store a and b in an appropriate data structure
    tree.add(a,b)
tree.solve()

print tree
