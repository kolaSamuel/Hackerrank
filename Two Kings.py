from copy import deepcopy as copy
import os
import sys

start_state = [[0]*8 for _ in range(8)]


def get_moves(x1, y1, x2, y2, moves):

    # adjust to increase search space
    span = 1

    for i in xrange(8):
        for j in xrange(8):

            if (i, j) in [(x1, y1), (x2, y2)]:
                continue
            if abs((x1-i)) <= span and abs(y1-j) <= span:
                moves.add(('Q', i, j))
            elif abs((x2-i)) <= span and abs(y2-j) <= span:
                moves.add(('Q', i, j))

            if abs((x1-i)*(y1-j)) == 2:
                moves.add(('N', i, j))
            elif abs((x2-i)*(y2-j)) == 2:
                moves.add(('N', i, j))


def is_mate(dfs, kings):

    for (x, y) in kings:
        for i in xrange(8):
            for j in xrange(8):
                if abs((x - i)) <= 1 and abs(y - j) <= 1:
                    if any(p == 'Q' and (ip == i or ip == j) for (p, ip, jp) in dfs):
                        continue
                    elif any(p == 'Q' and (jp == i or jp == j) for (p, ip, jp) in dfs):
                        continue
                    elif any(p == 'Q' and (abs(ip-i) == abs(jp-j)) for (p, ip, jp) in dfs):
                        continue
                    elif any(p == 'N' and (abs(ip-i) * abs(jp-j) == 2) for (p, ip, jp) in dfs):
                        continue
                    else:
                        return False
    return True


def play(move, state, dfs, result, kings, x=1):
    p, i, j = move
    if x == 1:
        dfs.add(move)
        if is_mate(dfs, kings):
            return list(dfs)
        return result
    else:
        dfs.remove(move)


def checkmate(x1, y1, x2, y2):
    game_state = copy(start_state)
    moves = set()
    get_moves(x1, y1, x2, y2, moves)
    dfs = set()
    king_span = [(x1, y1), (x2, y2)]
    result = [0, 0, 0, 0, 0]

    for one in moves:
        result = play(one, game_state, dfs, result, king_span)
        if len(result) > 2:
            for two in moves:
                # if ('N', i, j) or ('Q', i, j) in [one]:
                if two in dfs:
                    continue
                result = play(two, game_state, dfs, result, king_span)
                if len(result) > 3:
                    for three in moves:
                        if three in dfs:
                            continue
                        result = play(three, game_state, dfs, result, king_span)
                        if len(result) > 4:
                            for four in moves:
                                if four in dfs:
                                    continue
                                result = play(four, game_state, dfs, result, king_span)
                                play(four, game_state, dfs, result, None, -1)
                        play(three, game_state, dfs, result, None,  -1)
                play(two, game_state, dfs, result, None, -1)
        play(one, game_state, dfs, result, None, -1)

    # print x1, y1, x2, y2
    print len(result)
    for (p, i, j) in result:
        print p, i, j


if __name__ == '__main__':
    t = int(input())

    for t_i in range(t):
        x1y1x2y2 = raw_input().split()

        x1 = int(x1y1x2y2[0])
        y1 = int(x1y1x2y2[1])
        x2 = int(x1y1x2y2[2])
        y2 = int(x1y1x2y2[3])

        checkmate(x1, y1, x2, y2)



