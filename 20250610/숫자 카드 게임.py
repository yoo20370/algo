import sys

row, col = map(int, sys.stdin.readline().split())

# 각 행에서 가장 작은 값을 뽑아야 한다.
# 최대값을 저장하는 변수를 두고, 각 행을 순회하며, 최소값과 최소값 중 최대값을 비교한 후 결과 반환하게 구현하면 될 듯 

min_value_of_max = 0
for _ in range(row) :
    min_value = min(list(map(int, sys.stdin.readline().split())))

    min_value_of_max = max(min_value_of_max, min_value)

print(min_value_of_max)
