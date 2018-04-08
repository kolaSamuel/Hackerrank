# Enter your code here. Read input from STDIN. Print output to STDOUT
def validStates(pos):
    i,j = pos
    valid = []
    if j-2 < 16 and j-2 > 0:
        if i-1 > 0:valid.append((i-1,j-2))
        if i+1 < 16:valid.append((i+1,j-2))
    if i-2 < 16 and i-2 > 0:
        if j-1 > 0:valid.append((i-2,j-1))
        if j+1 < 16:valid.append((i-2,j+1))
    return valid

def solve(pos):
    global states
    if pos in states:
        return None
    solved =[]
    unsolved = []
    for x in validStates(pos):
        if x in states:solved.append(x)
        else:unsolved.append(x)
    if len(solved)==0 and len(unsolved)==0:
        states[pos]=0
    elif any(states[x]==0 for x in solved):
        states[pos]=1
    elif len(unsolved):
        for x in unsolved:
            solve(x)
            solve(pos)
    else:
        states[pos]=0
    
states = {(1,1):0}
for k in xrange(2,16):
    for i in xrange(k,k+1):
        for j in xrange(1,k):
            solve((i,j))
            solve((j,i))
        solve((i,i))
            
for _ in xrange(input()):
    i,j = map(int,raw_input().strip().split(' '))
    print 'First' if states[(i,j)] else 'Second'
