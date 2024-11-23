import sys
N, M = map(int, sys.stdin.readline().split())


check = [False] * N
# 열의 길이는 m, 행의 길이는 N 
def func(n, m, cnt, check, arr) :
    if m <= cnt  :
        for i in arr :
            print(i+1, end=" ")
        print()
        return 
    
    for i in range(N) :
        if check[i] == False :
            check[i] = True 
            arr.append(i)
            func(n, m, cnt+1, check, arr)
            arr.pop()
            check[i] = False 
    
func(N, M, 0, check, list())
    

    
        





    