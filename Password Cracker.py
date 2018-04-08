# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
def specialSplitter(x):
    x = list(x)
    string = "$".join(s for s in x) +' '
    return string

def normalizer(x):
    x = x.split('$')
    string = "".join(s for s in x)
    return string

for _ in xrange(input()):
    n = input()
    _passwords = raw_input().strip().split(' ')
    _crack_ = raw_input().strip()
    _passwords = permutations(_passwords,n)
    i = 0
    for passwords in _passwords:
        hacker = False
        crack = _crack_
        for x in passwords:
            _x = x +' '
            crack = crack.replace(x,specialSplitter(x))

        crack = normalizer(crack)
        _crack = set(crack.split(' '))
        passwords = set(passwords)
        for x in _crack:
            if not x in passwords and len(x):
                #print _crack
                hacker = True
                break
        if hacker == False :break
    print 'WRONG PASSWORD' if hacker else crack[:-1]
  
        
