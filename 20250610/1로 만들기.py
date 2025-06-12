import sys 

# 모든 경우의 수를 탐색해야하는 완전 탐색인 것 같다.
# 각 숫자에 대해서 가능한 모든 경우의 수를 확인한다. 그리고 각각 현재의 최소값과 경우의 수 + 1한 값 중 더 작은 것을 확인하는 방법으로 구현을 수행한다.

INF = int(1e5)

def make_one() :
    X = int(sys.stdin.readline().rstrip())

    memo = [INF] * (int(1e6) + 1)

    memo[1] = 0
    memo[2] = 1

    for curr in range(3, X + 1) :
        memo[curr] = min(memo[curr], memo[curr-1] + 1)

        if curr % 2 == 0 :
            memo[curr] = min(memo[curr], memo[curr // 2] + 1)

        if curr % 3 == 0 :
            memo[curr] = min(memo[curr], memo[curr // 3] + 1)

    return memo[X]

print(make_one())