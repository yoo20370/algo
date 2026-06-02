import sys

sys.setrecursionlimit(int(1e9))

memo = 0

def solution() :

    n = int(sys.stdin.readline().rstrip())

    global memo
     
    memo = [0] * (n + 1)

    # 1번째 항과 2번째 항은 둘 다 값이 고정되어 있으므로 
    memo[1] = 1
    memo[2] = 1

    print(fibo2(n))

# top_down 
def fibo(n) :

    global memo

    # fibo(1)과 fibo(2)의 경우 값을 계산하지 않도록 하기 위함 
    if n <= 2 :
        return memo[n]

    # 아직 계산된 경우 
    if memo[n] != 0 :
        return memo[n]
    
    # 계산이 되지 않은 경우 
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

# bottom_up
def fibo2(n) :
    global memo

    for i in range(3, n+1) :
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

solution()