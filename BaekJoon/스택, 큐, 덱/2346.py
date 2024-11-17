from collections import deque
import sys


N = int(sys.stdin.readline().rstrip())
listA = list(map(int, sys.stdin.readline().split()))
dequeue = deque()

for i in range(len(listA)) :
    dequeue.append([i, listA[i]])

while dequeue :
    idx, num = dequeue.popleft()
    print(idx+1, end=" ")

    if len(dequeue) > 1 :
        if num >= 0 :
            for _ in range(num - 1) :
                x, y = dequeue.popleft()
                dequeue.append([x,y])
        else :
            for _ in range(abs(num)) :
                x, y = dequeue.pop()
                dequeue.appendleft([x,y])

