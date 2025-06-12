import sys

# memo에 이전 값을 기록함, memo 값이 INF라는 것은 만들 수 없는 화폐라는 것 
# 각 memo에는 해당 화폐를 만들 수 있는 가장 작은 화폐 개수를 저장한다.
# 1원부터 목표 화폐까지 순서대로 순회하며, 화폐를 생성한다.
# 현재 화폐에서 coins를 순회하며 각각 빼주고 INF이면 넘어가고 INF가 아니라면, 현재 화폐의 최솟값과 현재 화폐 - coin의 최소값 + 1을 비교하여 더 작은 값을 기록한다. 

INF = int(1e5)
MX = 100001

def make_money() :
    coin_type_count, goal_money = map(int, sys.stdin.readline().split())

    memo = [INF] * MX
    
    coins = []
    for _ in range(coin_type_count) :
        coin = int(sys.stdin.readline().rstrip())
        coins.append(coin)
        memo[coin] = 1
        

    for curr_money in range(1, goal_money + 1) :
        for coin in coins :
            if memo[coin] != INF and curr_money - coin >= 1:
                memo[curr_money] = min(memo[curr_money], memo[curr_money - coin] + 1)
    
    result = memo[goal_money] if memo[goal_money] != INF else -1 
    return result

print(make_money())

    
