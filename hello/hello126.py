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

