# 반복되는 수열에 대해서 파악하는 것이 핵심 

import sys 

N, M, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort(reverse=True)

# 한 사이클 크기 
size = K+1

# 사이클 개수 
cycle = M // size

# 나머지 
remain = M % size

result = cycle * (data[0] * K + data[1])
result += remain * data[0]

print(result)