# 개미 전사
# 인접한 저장소 공격을 바로 알아차릴 수 있음 
# 결국 적어도 한 개 이상 떨어진 창고를 공격해야 함 

# n - 1의 식량 최대값과 n - 2와 n 약탈 식량 최대값 중 큰 값을 구해서 창고 약탈했을 때의 최대 식량값 구하면 됨 
# 그러면 DP 테이블에는 현재 창고까지를 털었을 때의 최대값을 저장하면 됨 
import sys

maxSize = 100

def solution() :
    n = int(sys.stdin.readline().rstrip())

    stores = list(map(int, sys.stdin.readline().split()))

    dp = [-1] * (n)
    dp[0] = stores[0]
    dp[1] = max(stores[0], stores[1])

    for i in range(2, n) :
        dp[i] = max(stores[i] + dp[i-2], dp[i-1])
    
    print(dp[n-1])

solution()
        


