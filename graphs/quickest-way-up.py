# https://www.hackerrank.com/challenges/the-quickest-way-up
# This is not the complete solution


def init_board():
    board = dict(enumerate(list(range(2, 101)), start=1))
    for key in board:
        board[key] = [board[key]]
    board[100] = []
    return board


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


def find_moves(path):
    if not path:
        return -1
    moves = 0
    i = 0
    # [1, 2, 54, 55, 33, 34, 35, 36, 100]
    while i < len(path):
        j = i + 1
        while j < len(path) and abs(path[j] - path[j - 1]) < 3:
            j += 1
        moves += int((path[j - 1] - path[i]) / 6) + 1
        i = j
    if(path[-1] - path[-2]) > 6:
        moves -= 1
    return moves

# jumps = {}
trap = []
T = int(input().strip())
for t in range(T):
    board = init_board()
    N = int(input().strip())
    for n in range(N):
        ladder = input().strip().split(' ')
        board[int(ladder[0]) - 1] = [int(ladder[1]), int(ladder[0]) + 1]
        # jumps[int(ladder[0])] = int(ladder[1])
    M = int(input().strip())
    for m in range(M):
        snake = input().strip().split(' ')
        if 100 - int(snake[0]) < 7:
            trap.append(int(snake[0]))
        board[int(snake[0]) - 1] = [int(snake[1]), int(snake[0]) + 1]
        # jumps[int(snake[0])] = int(snake[1])
    if len(trap) == 6:
        print(-1)
    else:
        path = find_shortest_path(board, 1, 100)
        print(find_moves(path))
