from collections import defaultdict
class node(object):
    def __init__(self):
        self.branch = defaultdict(node) 
        self.health = 0
        
    def __getitem__(self,x):
        return self.branch[x]
    
    def gets(self,x):
        if x in self.branch:
            return self.branch[x]
        return None
        
class trie(object):
    def __init__(self):
        self.tree = node()
        
    def add(self,s,x):
        current = self.tree
        for y in s:
            current = current[y]
        current.health += x
        
    def find(self,s):
        end = len(s)
        totalHealth = 0
        for i in xrange(end):
            current = self.tree
            for j in xrange(i,end):
                current = current.gets(s[j])
                if current == None:
                    break
                totalHealth+=current.health
        return totalHealth
                
n = input()
genes = raw_input().strip().split(' ')
health = map(int, raw_input().strip().split(' '))
mn,mx = float('inf'),float('-inf')
for _ in xrange(input()):
    first,last,d = raw_input().strip().split(' ')
    first,last,d = [int(first),int(last),str(d)]
    # your code goes here
    DNA = trie()
    for i in xrange(first,last+1):
        DNA.add(genes[i],health[i])
    DNA_Health = DNA.find(d)
    mn = min(DNA_Health,mn)
    mx = max(DNA_Health,mx)
print mn,mx
