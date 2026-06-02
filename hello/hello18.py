# 나누어 떨어지는지 먼저 확인해야 할 듯
# 26 -> 나누어 떨어짐 ?? -> ㄴㄴ -> -1해 
# 25 -> 나누어 떨어짐 ?? -> oo -> 나눠 
# 5 -> 나누어 떨어짐 ?? -> oo -> 나눠
# 1 -> 끝 

# 1로 만드는 최소값을 구해야함 
# 결국 이 말은 모든 경우의 수를 구하고 그 중에서 가장 적은 횟수를 골라야 한다는 것
# 근데 여기서 중요한 건 특정 값들은 구하는데 여러 방법이 있을 것
# 그 중에서 가장 작은 횟수를 생각하고 현재 x의 최소 횟수를 구해야함 

# 어떻게 풀거야 ?? 
# x가 1이 되는 경우를 구할 때, 모든 경우의 수를 생각한다. 
# 그리고 x를 구할 수 있는 방법은 최대 4가지가 될 수 있음 (a * 5, a * 3, a * 2, a + 1)
# 이 중 만들 수 있는 수중 최소한의 값을 구해서 반환하면 됨 
# 이때 x가 1이라면 구할 수 있는 방법은 0
# 그래서 makeNumberOne 함수는 현재 x에 대해서 최소로 구할 수 있는 방법을 찾아서 반환하면 됨, 이때 그 결과에 1을 더해주면 됨 -> 연산 한 번을 수행해야 현재 x값에 도달하기 때문 

import sys
maxValue = 30000
INF = int(1e9)

# -1은 아직 계산되지 않은 경우 
memo = [INF] * (maxValue + 1)


memo[1] = 0

def solution() :

    inputValue = int(sys.stdin.readline().rstrip())

    result = makeNumberOne2(inputValue)
    print(result)

# TopDown 방식 
def makeNumberOne(x) :

    if x == 1 :
        return 0
    
    if memo[x] != INF :
        return memo[x]
    
    minCount = INF

    if x % 5 == 0 :
        result = makeNumberOne(x // 5)
        minCount = min(minCount, result + 1)

    if x % 3 == 0 :
        result = makeNumberOne(x // 3)
        minCount = min(minCount, result + 1)

    if x % 2 == 0 :
        result = makeNumberOne(x // 2)
        minCount = min(minCount, result + 1)

    result = makeNumberOne(x - 1)
    memo[x] = min(minCount, result + 1)

    return memo[x]

    
def makeNumberOne2(x) :
    
    # 1은 0이니까 구할 필요 없고 2부터 최대값까지 각 숫자의 최소값을 구하도록 하면 될 것이라 생각 
    for i in range(2, x + 1) :

        # i - 1은 무조건 값이 있음 그러므로 이 값을 기준으로 시작하려고 함 
        memo[i] = memo[i-1] + 1
        
        # elif가 아니라 if로 하는 이유는 현재 어떤 값으로 나눠야 최소값이 되는지 결정되지 않기 때문 -> 어떤 순서로 나눴을 때, 최소값이 나오는지 모르기 때문 
        # 왜 큰 숫자부터 ?? 기준이 없긴함..... 그냥 내림차순으로 진행 
        if i % 5 == 0 :
            result = memo[i // 5] + 1
            memo[i] = min(memo[i], result)
        
        if i % 3 == 0 :
            result = memo[i // 3] + 1
            memo[i] = min(memo[i], result)

        if i % 2 == 0 :
            result = memo[i // 2] + 1
            memo[i] = min(memo[i], result)

    return memo[x]

    
solution()