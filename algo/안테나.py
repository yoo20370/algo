import sys 

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

print(data[(N-1) // 2])