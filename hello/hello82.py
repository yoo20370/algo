# 특정 프로세스가 몇 번째로 실행되는지 알아내라

# 실행 대기 큐에서 대기중인 프로세스 하나를 꺼낸다.
# 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣는다.
# 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행한다.
# 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료된다. 

# 최대값을 구하는 것을 순회하지 말고 우선순위 큐를 사용해도 될 듯 

import heapq
from collections import deque

def solution(priorities, location):
    
    queue = deque()
    
    priorityQueue = []
    
    for index in range(len(priorities)) :
        queue.append((index, priorities[index]))
        heapq.heappush(priorityQueue, -priorities[index])
    
    count = 0 
    while queue :
        currentIndex, currentPriority = queue.popleft()
        
        maxPriorty = -priorityQueue[0]
        if  maxPriorty > currentPriority :
            queue.append((currentIndex, currentPriority))
            continue
        
        count += 1
        if location == currentIndex :
            return count 
        
        heapq.heappop(priorityQueue)
            
