import sys
from collections import deque

def knight_movement() -> None:

    N = int(sys.stdin.readline().rstrip())

    graph = [ [0] * N for _ in range(N)]

    start_r, start_c = map(int, sys.stdin.readline().split())

    end_r, end_c = map(int, sys.stdin.readline().split())

    if start_r == end_r and start_c == end_c :
        print(0)
        return

    distance = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    queue = deque()
    queue.append([start_r, start_c])
    graph[start_r][start_c] = 0

    while queue :
        curr_r, curr_c = queue.popleft()

        for d_r, d_c in distance :
            n_r = curr_r + d_r 
            n_c = curr_c + d_c

            if n_r >= 0 and n_r < N and n_c >= 0 and n_c < N and graph[n_r][n_c] == 0 :
                graph[n_r][n_c] = graph[curr_r][curr_c] + 1
                queue.append([n_r, n_c])

    print(graph[end_r][end_c])


T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    knight_movement()