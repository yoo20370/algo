from collections import deque
import sys 

def bfs(start_row, start_col, max_row, max_col, pan_data) -> None : 

    # 동서남북
    distance = [(0,1), (0,-1), (1,0), (-1,0)]
    
    queue = deque()
    queue.append((start_row, start_col))

    while queue :
        curr_row, curr_col = queue.popleft()
        pan_data[curr_row][curr_col] = 1

        for row, col in distance :
            now_row = curr_row + row
            now_col = curr_col + col

            if now_row >= 0 and now_row < max_row and now_col >= 0 and now_col < max_col and pan_data[now_row][now_col] == 0:
                queue.append((now_row, now_col))

max_row, max_col = map(int, sys.stdin.readline().split())

pan_data = []

# 2차원 배열을 전부 순회한다.
# 카운트 값을 1 증가시킨다. 
# 0을 만나면 bfs를 수행하여 모두 1로 바꿔준다.
# 2차원 배열을 모두 순회하면 카운트 값을 반환한다. 
for _ in range(max_row) :
    pan_data.append(list(map(int, sys.stdin.readline().rstrip())))

total_count = 0
for r in range(max_row) :
    for c in range(max_col) :
        if pan_data[r][c] == 0 :
            total_count += 1
            bfs(r, c, max_row, max_col, pan_data)

print(total_count)

