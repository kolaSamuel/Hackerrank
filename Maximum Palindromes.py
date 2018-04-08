mod = 10**9 + 7
string = input().strip()
q = int(input())

array = [[0]*(len(string)+1) for _ in range(26)]
fact_length = (len(string)+2)//2
fact = [1]*fact_length
fact_inv = [1]*fact_length


def initialize():
    # initialize factorial
    for i in range(2, len(fact)):
        fact[i] = (fact[i-1]*i) % mod
        fact_inv[i] = pow(fact[i], mod-2, mod)
    for i in range(len(string)):
        affected = ord(string[i]) - ord('a')

        for j in range(26):
            array[j][i] += array[j][i-1]
        array[affected][i] += 1


initialize()

for _ in range(q):
    odd, even = 0, []
    l, r = [int(x)-1 for x in input().split()]
    for i in range(26):
        count = array[i][r] - array[i][l-1]
        odd += int(count & 1)
        even.append(count//2)

    odd = max(odd, 1)
    total = fact[sum(even)] * odd
    for x in even:
        total *= fact_inv[x]
        total %= mod
    total %= mod
    print(total)
