# 열쇠는 회전과 이동이 가능 
# 열쇠 돌기 부분을 자물쇠 홈 부분에 딱 맞게 채우면 자물쇠가 열리는 구조 
# 좌물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 좌물쇠를 여는데 영향을 주지 않는다.
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물소의 홈 부분 정확히 일치해야 하며
# 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안 됩니다. 

##################################################################
# 회전을 수행하고 키를 이동시켜가며 Lock에 맞는지 확인해야함 
# 키는 항상 좌물쇠보다 작음 

def turn(key) :
    M = len(key)
    
    turn_key = [[0] * M for _ in range(M)]
    for r in range(M) :
        for c in range(M) :
            turn_key[c][M-1-r] = key[r][c]
    
    return turn_key

def check(lock, key, N) :
    
    for r in range(N) :
        for c in range(N) :
            if lock[r][c] + key[r][c] != 1 :
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    dr = [-1, 1]
    dc = [-1, 1]
    
    for _ in range(4) :
        key = turn(key)
            
        # 현재 키를 기준으로 이동시키면서, 열 수 있는지 확인 
        for move_r in dr :
            for move_c in dc :
                for i in range(0, N,1) :
                    for j in range(0, N,1) :
                        new_key = [[0] * N for _ in range(N)] 
                        for curr_r in range(M) :
                            for curr_c in range(M) :
                                next_row = curr_r + (move_r * i)
                                next_col = curr_c + (move_c * j)
                                # 벗어나지 않은 경우만 이동 
                                if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N :
                                    new_key[next_row][next_col] = key[curr_r][curr_c]

                        if check(new_key, lock, N) :
                            return True
                
    return False

