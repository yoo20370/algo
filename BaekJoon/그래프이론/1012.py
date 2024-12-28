import sys
from collections import deque
def bfs(farm_map, row, col, max_r, mac_c) -> None :

    # 동, 서, 남, 북
    distance = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 방문 처리 
    farm_map[row][col] = 0
    queue = deque()
    queue.append([row, col])

    while queue :
        curr_r, curr_c = queue.popleft()

        for d_r, d_c in distance :
            n_r = curr_r + d_r
            n_c = curr_c + d_c

            if n_r >= 0 and n_c >= 0 and n_r < max_r and n_c < mac_c and farm_map[n_r][n_c] == 1 :
                farm_map[n_r][n_c] = 0
                queue.append([n_r, n_c])
    

def remove_bug() -> None:
    col, row, cnt = map(int, sys.stdin.readline().split())

    farm_map = [[0] * (col) for _ in range(row)]

    for _ in range(cnt) :
        c, r = map(int, sys.stdin.readline().split())
        farm_map[r][c] = 1
    

    cnt = 0
    for i in range(row) :
        for j in range(col) :
            if farm_map[i][j] == 1 :
                bfs(farm_map, i, j, row, col)
                cnt += 1
    
    print(cnt)

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    remove_bug()
        

