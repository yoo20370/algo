# Top-Down 방식
# import sys

# N = int(sys.stdin.readline().rstrip())

# dp = [-1] * (N+1) 

# def makeOne(n) -> int:
#     if n == 1 :
#         return 0
    
#     if dp[n] != -1 :
#         return dp[n]
    
#     result = makeOne(n-1)
#     if n % 5 == 0 :
#         result = min(result, makeOne(n//5))
#     if n % 3 == 0 :
#         result = min(result, makeOne(n//3))
#     if n % 2 == 0 :
#         result = min(result, makeOne(n//2))

#     # 이전의 최소값과 앞으로 수행할 연산인 1을 더해 연산의 수를 계산한다. 
#     dp[n] = result + 1
#     return dp[n]

# print(makeOne(N))

# Bottom-Up 방식
import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N+1)

def makeOne(n) -> None :

    for idx in range(2,n+1):
        dp[idx] = dp[idx-1] + 1
        if idx % 5 == 0 :
            dp[idx] = min(dp[idx], dp[idx//5] + 1)
        if idx % 3 == 0 :
            dp[idx] = min(dp[idx], dp[idx//3] + 1)
        if idx % 2 == 0 :
            dp[idx] = min(dp[idx], dp[idx//2] + 1)
        
makeOne(N)
print(dp[N])