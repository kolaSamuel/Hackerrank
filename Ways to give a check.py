from collections import _heapq as heapq

N = input()
Mason = input()
height = map(int, raw_input().split())
cost = map(int, raw_input().split())
_min = [''] * (N - 1)
fringe = []
node = (0, 0, Mason)

while 1:
    print node
    score, pos, h = node
    if pos < N-1 and score <= _min[pos]:
        _min[pos] = score
        new_score = cost[pos] + score + abs(h-height[pos])
        pos += 1
        if h >= height[pos - 1]:
            heapq.heappush(fringe, (score, pos, h))
        heapq.heappush(fringe, (new_score, pos, height[pos - 1]))
    if len(fringe) == 0:
        break
    node = heapq.heappop(fringe)

print score + N
