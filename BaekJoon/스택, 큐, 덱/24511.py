# 1차시도 시간복잡도 O(N^2)
# 그러므로 해시 테이블 사용해보려 함 

from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

# 스택 혹은 큐이므로 dequeue를 사용한다. 
dequeue = deque([deque() for i in range(N)])

# 스택인지 큐인지 
typeList = list(map(int, sys.stdin.readline().split()))

# 각 자료구조에 어떤 원소가 들어있는지 
dataList = list(map(int, sys.stdin.readline().split()))

# 넣을 때는 큐나 스택이나 뒤로 들어가기 때문에 조건 검사 필요 없음 
for i in range(N) :
    dequeue[i].append(dataList[i])

# 수열의 길이가 주어진다. 
M = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().split()))

def queuestack(N, dequeue, typeList, temp) :
    for i in range(N) :
        # n-1번째 자료구조에 삽입 
        dequeue[i].append(temp)

        # n번째 자료구조에 삽입할 xn-1을 꺼내는 작업 
        if typeList[i] == 0 :
            temp = dequeue[i].popleft()
        else :
            temp = dequeue[i].pop()
    return temp 

for z in range(M) :
    print(queuestack(N, dequeue, typeList, numList[z]), end=" ")

## 큐와 스택을 
from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

# 스택 혹은 큐이므로 dequeue를 사용한다. 
dequeue = deque()

# 스택인지 큐인지 
typeList = list(map(int, sys.stdin.readline().split()))

# 각 자료구조에 어떤 원소가 들어있는지 
dataList = list(map(int, sys.stdin.readline().split()))

# 넣을 때는 큐나 스택이나 뒤로 들어가기 때문에 조건 검사 필요 없음 
for i in range(N) :
    if typeList[i] == 0 :
        dequeue.append(dataList[i])
    
# 수열의 길이가 주어진다. 
M = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().split()))

for i in numList :
    dequeue.appendleft(i)
    print(dequeue.pop(), end=" ")

