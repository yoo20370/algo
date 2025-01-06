import sys, heapq

N, M = map(int, sys.stdin.readline().split())

entry_cnt = [0] * (N+1)
edegs = [ [] for i in range(N+1)]

for _ in range(M) :
    start, end = map(int, sys.stdin.readline().split())
    entry_cnt[end] += 1
    edegs[start].append(end)

def func() -> None :

    queue = list()

    for i in range(1, N+1) :
        if entry_cnt[i] == 0 :
            heapq.heappush(queue, i)
    
    while queue :
        curr = heapq.heappop(queue)
        print(curr, end=" ")

        for end in edegs[curr] :
            entry_cnt[end] -= 1
            if entry_cnt[end] == 0 :
                heapq.heappush(queue, end)

func()