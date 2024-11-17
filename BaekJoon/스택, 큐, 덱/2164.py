from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())

queue = deque()
for i in range(1, N + 1) :
    queue.append(i)

while len(queue) != 1 :
    # 제일 위에 있는 카드를 버린다.
    queue.popleft()
    # 현재 제일 위에 있는 카드를 뽑아서 맨 아래로 내린다.
    data = queue.popleft()
    queue.append(data)

print(queue[0])
    

