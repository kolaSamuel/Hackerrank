from math import pow
import fractions
X = input()
N = input()
lim = int(X**(1.0/N))+1
count = [0]


def solve(i, total=0):
    if total > X:
        return None
    elif total == X:
        count[0] += 1
        return
    for j in xrange(i, lim):
        print '\t'*i + ' j ' + str(j) + ' tot ' + str(total)
        solve(j+1, pow(j, N)+total)

solve(0)
print count[0]