import sys

# 가로 사이즈가 1 작은 것을 모두 가지고 있다. 2 * 1 막대를 마지막에 두면 나머지 부분은 가로 사이즈가 1 작은 것과 동일한 개수를 만들 수 있다.
# 또한 2 * 2를 만들 수 있는 경우의 수는 3가지이다. 이 때, 2 * 1 2개로 만든 것은 가로 사이즈가 1 작은 것에 포함되므로 제외
# 점화식 f(n-1) + f(n-2) * 2

N = int(sys.stdin.readline().rstrip())

memo = [0] * (N + 1) 

memo[1] = 1
memo[2] = 3

for i in range(3, N+1) :
    memo[i] = (memo[i - 1] + memo[i - 2] * 2) % 796796

print(memo[N])