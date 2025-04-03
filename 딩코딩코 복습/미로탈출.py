from collections import deque
import sys 

max_row, max_col = map(int, sys.stdin.readline().split())

miro_data = []

for _ in range(max_row) :
    miro_data.append(list(map(int, sys.stdin.readline().rstrip())))




def escape_miro(max_row, max_col, miro_data) -> int :

    # 동, 서, 남, 북 
    distance = [(0,1), (0,-1), (1,0), (-1,0)]

    queue = deque()
    queue.append((0,0,0))

    while queue :
        curr_row, curr_col, cost = queue.popleft()
        miro_data[curr_row][curr_col] = cost + 1

        for row, col in distance :
            now_row = curr_row + row
            now_col = curr_col + col

            if now_row >= 0 and now_row < max_row and now_col >= 0 and now_col < max_col and miro_data[now_row][now_col] == 1 :
                queue.append((now_row, now_col, miro_data[curr_row][curr_col]))
    
    return miro_data[max_row - 1][max_col - 1] 


print(escape_miro(max_row, max_col, miro_data))