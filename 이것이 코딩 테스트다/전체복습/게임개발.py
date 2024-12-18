import sys
# 1.  현재 위치에서 현재방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.

# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 
# 왼쪽 방향으로 회전한 다음 외쪽으로 한 칸을 전진한다. 
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다. 

# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
# 단, 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 엇ㅂ는 경우 움직임을 멈춘다.

def gameDev() -> int :
    # 북쪽, 동쪽, 남쪽, 서쪽
    distance = [0, 1, 2, 3]

    # 바라보는 방향의 왼쪽 위치를 위한 좌표
    leftX = [-1, 0, 1, 0]
    leftY = [0, -1, 0, 1]

    # 왼쪽으로 돌았을 때, 바라보는 방향
    turn_left = [3, 0, 1, 2]

    # 뒤로가기 위한 좌표, 음수 처리시 앞으로 가기 위한 좌표
    back_stepX = [0, -1, 0, 1]
    back_stepY = [1, 0, -1, 0]

    # row는 세로 길이, column은 가로 길이 
    row, column = map(int, sys.stdin.readline().split())

    X, Y, dis = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(row) :
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 첫 위치 방문 처리 
    cnt = 1 
    graph[X][Y] = -1
    
    turn_cnt = 0
    currDis = dis    
    while True :
                
        nx = X + leftX[currDis]
        ny = Y + leftY[currDis]

        # 왼쪽 위치 확인
        if graph[nx][ny] == 0 :
            
            # 회전하기
            currDis = turn_left[currDis]
            
            # 이동한 곳으로 설정 
            graph[nx][ny] = -1

            # 앞으로 한 칸 이동 
            X = nx
            Y = ny
            cnt += 1 

            # 이동 했으므로 회전 초기화 
            turn_cnt = 0 


        # 왼쪽이 갈 수 없는 경우 
        else :
            # 한 바퀴 회전한 경우 
            if turn_cnt == 4 :
                nx = X - back_stepX[currDis]
                ny = Y - back_stepY[currDis]
                
                # 뒤로 이동했는데 바다인 경우 
                if graph[nx][ny] == 1 :
                    return cnt  
                    
                else :
                    # 바다가 아닌 경우 뒤로 이동 
                    X = nx
                    Y = ny
                    
                    # 이동 했으므로 회전 초기화 
                    turn_cnt = 0
            else : 
                # 회전하기
                currDis = turn_left[currDis]    
                turn_cnt += 1
                

        # 왼쪽이 갈 수 있는 경우 
        
print(gameDev())