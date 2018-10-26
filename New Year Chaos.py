

def minimumBribes(q, result=0, index=1):
    size = len(q)

    if size <= 1:
        if q[0] - index > 2:
            return float('inf')
        return result

    l = size // 2
    r = size - l
    left, right = q[:l].copy(), q[l:].copy()
    result = minimumBribes(left, result, index)
    result = minimumBribes(right, result, index + l)

    i, j = 0, 0
    while i < l and j < r:
        if left[i] < right[j]:
            q[i + j] = left[i]
            i += 1
        else:
            q[i + j] = right[j]
            j += 1
            result += (l - i)

    for k in range(i, l):
        q[k + j] = left[k]
    for k in range(j, r):
        q[i + k] = right[k]

    return result


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        Q = list(map(int, input().rstrip().split()))
        answer = minimumBribes(Q)
        print(answer if answer != float('inf') else 'Too chaotic')
