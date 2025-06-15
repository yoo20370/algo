import sys 

# 점화식이 f(n-1) + f(n-2)
# -> 이전 타일에 1을 붙이는 경우와 전전 타일에 00을 붙이는 경우 현재 타일의 길이가 됨 
# 1 타일과 00 타일로 만들어야 함 

tile_count = int(sys.stdin.readline().rstrip())

memo = dict()

memo[1] = 1
memo[2] = 2

for count in range(3, tile_count + 1) :
    memo[count] = (memo[count - 1] + memo[count - 2]) % 15746

print(memo[tile_count])






