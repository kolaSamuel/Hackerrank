# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def sGene(start,stop,step,goal,steady = Counter(),count = 0):
    global gene
    for i in xrange(start,stop,step):
        dna = gene[i]
        if steady[dna] < goal: 
            steady[dna]+=1
            count+=1
        else:return (count,steady,i)
            
length = input()
goal = length/4
gene = raw_input().strip()

count,steady,dummy = sGene(0,length,1,goal)
icount = count
best = count
pos = length-1
if count ==length:icount=0
for i in xrange(icount-1,-1,-1):
    steady[gene[i]]-=1
    count,steady,pos = sGene(pos,-1,-1,goal,steady,count-1)
    best = max(best,count)
    #print 'check',count,i
print length-best
