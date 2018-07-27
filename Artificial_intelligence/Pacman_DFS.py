import sys
inp = lambda x: list(map(int, x.split()))

pac_man = inp(input())
dot = tuple(inp(input()))
world = inp(input())
world_map = [input() for _ in range(world[0])]

pos = (pac_man[0], pac_man[1])
dfs = [pos]
optimal_dfs = [pos]
visited = set(dfs)
direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def solve(pac_man):
    for (x, y) in direction:
        _x = x + pac_man[0]
        _y = y + pac_man[1]
        if world_map[_x][_y] != '%':
            if not ((_x, _y) in visited):
                pos = (_x, _y)
                dfs.append(pos)
                optimal_dfs.append(pos)
                visited.add(pos)
                if pos == dot or solve(pos):
                    return True
                optimal_dfs.pop()

    return False


solve(pac_man)
for (i, x) in enumerate([dfs, optimal_dfs]):
    print(len(x)-i)
    for pos in x:
        print(*pos)