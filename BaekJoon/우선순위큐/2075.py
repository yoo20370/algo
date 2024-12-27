import sys, heapq

N = int(sys.stdin.readline().rstrip())

data = list()
for _ in range(N) :
    for i in list(map(int, sys.stdin.readline().split())) :
        heapq.heappush(data, -i)

for item in range(N) :
    result = - heapq.heappop(data)

print(result)