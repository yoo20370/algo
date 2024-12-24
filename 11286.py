import sys, heapq

N = int(sys.stdin.readline().rstrip())

heap = list()

for _ in range(N) :
    data = int(sys.stdin.readline().rstrip())
    if data == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            a, b = heapq.heappop(heap)
            print(b)
    else :
        heapq.heappush(heap, (abs(data), data))    