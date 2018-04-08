# Enter your code here. Read input from STDIN. Print output to STDOUT
def skipsTown(house,paths):
    result = 0
    for x in paths[house]:
        result += 1<<(x-1)
    return result

def Killgrave(N,paths,C,money = 0,_max = 0,count = 1,travels = 0,notHome = 0):
    global visited
    global A
    goal = (1<<N)-1
    if travels | notHome == goal:
        return (_max,count)
 
    for i in A:
        house = i+1
        location = 1<<i
        if location & travels:continue
        if location & notHome:continue
        if travels|location in visited:continue
        skips = skipsTown(house,paths)
        visited.add(travels|location)
        collected = money+C[i]
        if collected > _max:
            _max,count = collected,1
        elif collected == _max:
            count +=1
        _max,count = Killgrave(N,paths,C,collected,_max,count,travels|location,notHome|skips)

    return (_max,count)

visited = set()
N,M = map(int,raw_input().strip().split())
C = map(int,raw_input().strip().split())
paths = [[] for _ in xrange(N+1)]
for _ in xrange(M):
    u,v = map(int,raw_input().strip().split())
    paths[u].append(v)
    paths[v].append(u)
A = []
bonus,mul = 0,1
seen = []
extra =[0,1]#bonus,mul
for i in xrange(1,N+1):
    if i in seen:continue
    if len(paths[i])==1 and len(paths[paths[i][0]])==1:
        j = paths[i][0]
        seen.append(j)
        special = max(C[i-1],C[j-1])   
        if special:
            bonus+=special
            if C[i-1]==C[j-1]:
                extra[0]+=2
        else:extra[1]*=3
    elif len(paths[i]):A.append(i-1)
    elif C[i-1] == 0:mul<<=1
    elif C[i-1]:
        bonus+=C[i-1]
extra[0]=max(extra[0],1)
cost,count = Killgrave(N,paths,C)
print cost+bonus,count*mul*extra[1]*extra[0]
