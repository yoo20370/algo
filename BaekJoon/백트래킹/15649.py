import sys
N, M = map(int, sys.stdin.readline().split())


bm = [False] * N
# 열의 길이는 m, 행의 길이는 N 
def func(m, s ,bm) :
    if s == N :
        return
    for _ in range(m) :
        if False == bm[s] :
            bm[s] = True
            print(s+1, end=" ")
            func(m, s+1, bm)
            bm[s] = False

func(M, 0, bm)
    

    
        





    