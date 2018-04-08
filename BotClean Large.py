def is_valid(pos, move, board, dim):
    for i in range(2):
        if not (0 <= pos[i] + move[i] < dim[i]):
            return False
    return True


def next_move(posx, posy, dimx, dimy, board):
    dim = (dimx, dimy)
    pos = [posx, posy]
    dirty = 0
    for row in board:
        for x in row:
            if x == 'd':
                dirty += 1
    if board[posx][posy] == 'd':
        print("CLEAN")
        return

    best = {'LEFT': '', 'RIGHT': '', 'UP': '', 'DOWN': ''}
    moves = {'LEFT': (-1, 0), 'RIGHT': (1, 0), 'UP': (0, -1), 'DOWN': (0, 1)}

    best_state = {}
    for move in moves:
        if is_valid(pos, move, board, dim):
            pos[0] += move[0]
            pos[1] += move[1]
        else:
            continue

    print("")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
