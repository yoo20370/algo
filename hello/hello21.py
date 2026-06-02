# 효율적인 화폐 구성 
# 화폐들의 개수를 최소한으로 사용해서 그 가치의 합이 M원이 되도록 하려고 함
# 이때 각 화폐는 몇 개라도 사용할 수 있음

import sys

def func(n) :

    if dp[n] != INF :
        return dp[n]
    
    minCount = INF 
    for coin in coins :
        if n >= coin :
            result = func(n - coin)
            minCount = min(minCount, result + 1)

    dp[n] = minCount
    return dp[n]


maxSize = 10000

INF = int(1e9)

coinCount, targetMoney = map(int, sys.stdin.readline().split())

coins = []

dp = [INF] * (targetMoney + 1)
dp[0] = 0

for _ in range(coinCount) :
    coins.append(int(sys.stdin.readline().rstrip()))        

result = func(targetMoney)
if result == INF :
    print(-1)
else :
    print(result)


# 두 가지가 있지 않나 ?? 이 화폐를 만들 수 있을 수도 없을 수도 있음 
# 그리고 만들 수 있는 경우 
# 이건 Topdown으로 풀어야 함 -> 모든 경우를 구하는게 아니고 가능한 경우만 풀어야 함 
# 예를 들어 15를 구해야하는데 15에 도달 할 수 있도록 만들 수 없다면 -> 15에서 코인의 조합을 아무리 해도 안 되는 경우가 있음 이러면 -1 반환하면 됨 
# BottomUp 방식처럼 다 구할 필요가 없음 

# 솔직히 쉽게 말하면 targetMoney를 구할 수 있는 모든 방법을 구하고 그 중 최소값을 찾아내면 되는 문제 

# 그럼 일단 coins을 돌려서 dp에 채우자 -> 각 코인은 해당 가격으로 1개로 만들 수 있으니까 
# 만약 2, 3 코인이 있고 13을 만들라고 했을 때를 생각해보자
# 11, 10을 구할 수 있는데 이중 최소값을 가져와서 + 1하면 됨 이를 반복하면 됨 -> 11 -> 9, 8 
# 해당 숫자를 구할 수 없다면 -1을 리턴하고

