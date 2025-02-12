import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

s_row, s_col, s_dis = map(int, sys.stdin.readline().split())

graph = []

for _ in range(row) :
    graph.append(list(map(int, sys.stdin.readline().split())))

def robot_vacuum_cleaner(row, col, s_row, s_col, s_dis, graph) -> int :

    # 이동하자마다 청소하지 않은 구역이라면 청소를 수행한다.
    # 큐에는 다음 이동할 칸을 넣는 것이다. 
    # 회전한 후(turn_left), 바로 앞 칸(move_forward)이 청소가 되어 있지 않다면 큐에 row, col, dis를 삽입하고 반복문 탈출 
    # 사방면을 모두 확인했음에도 불구하고, 청소할 수 있는 영역이 없다면 뒤로 이동한다. (큐에 뒤로 이동 좌표 삽입)
    # 이 때 뒤가 벽(1)인 경우 외부 반복문을 탈출한다.

    # 북, 동, 남, 서
    distance = [0, 1, 2, 3]
    turn_left = [3, 0, 1, 2]
    move_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque()
    queue.append((s_row, s_col, s_dis))
    
    clean_count = 0
    while queue :
        c_row, c_col, c_dis = queue.popleft()

        if graph[c_row][c_col] == 0 :
            graph[c_row][c_col] = -1
            clean_count += 1
        
        dis = c_dis
        for _ in range(4):
            # 회전 
            dis = turn_left[dis]

            # 앞으로 이동 
            n_row, n_col = move_forward[dis]

            d_row = c_row + n_row
            d_col = c_col + n_col

            # 청소가 가능하다면
            if d_row >= 0 and d_col >= 0 and d_row < row and d_col < col and graph[d_row][d_col] == 0 :
                queue.append((d_row, d_col, dis))
                break

        # 플래그 변수를 사용하면 코드가 복잡해질 것 같아서 for else 사용 
        else : 
            # 뒤로 이동 
            n_row, n_col = move_forward[c_dis]
            d_row = c_row - n_row
            d_col = c_col - n_col 

            if graph[d_row][d_col] == 1 :
                break
            
            queue.append((d_row, d_col, c_dis))
                
    return clean_count

print(robot_vacuum_cleaner(row, col, s_row, s_col, s_dis, graph))