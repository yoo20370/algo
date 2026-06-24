# 한 번에 하나의 작업만 수행 할 수 있다.

## 작업 요청이 들어오면, 
# 작업의 번호, 작업의 요청 시각, 작업의 소요 시간을 저장해 두는 대기 큐 존재 
# 처음에 대기 큐는 비어 있다.

## 디스크 컨트롤러는 하드디스크가 작업을 하고 있지 않고 대기 큐가 비어 있지 않다면
# 가장 우선순위가 높은 작업을 대기 큐에서 꺼내 하드디스크에 작업을 시킨다. 

## 하드 디스크는 작업을 한 번 시작하면, 작업을 마칠 때까지 그 작업만 수행 

# 하드디스크가 어떤 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면
# 하드디스크 작업을 마치자마자,
# 디스크 컨트롤러는 요청이 들어온 작업을 대기 큐에 저장한 뒤, 우선순위가 높은 작업을 대기 큐에서 꺼내 하드디스크에 그 작업을 시킨다. 

# 하드디스크가 어떤 작업을 마치는 시점에 다른 작업이 들어오지 않더라도 그 작업을 마치자마자 또 다른 작업을 시작할 수 있다.

# 지금 보면 소요되는 시간이 우선순위인 것 같음 
# 그것에 대한 이야기가 없음 

# 어떻게 처리하냐면 
# 처음에 0ms 시점에 시작하는 모든 작업을 heap에 넣는다. 
# 작업을 꺼내서 진행한다. 종료시점을 기록한다. 
# 현재 시간을 기준으로 순회해서 대기큐에 삽입한다. (visited라는 set()을 둬서 이미 접근한 것은 제외할 예정)

# 이 과정을 모든 작업을 처리할 때까지 기다린다.
# 만약 중간에 유후상태가 되는 건 어떻게 처리할 것인가 ??
## 아직 모든 작업을 처리하지 않았고, 대기큐가 비어있다면 -> 유후 상태가 됨 이때는 가장 가까운 시작 시간을 갖는 녀석을 힙에 넣어서 진행하도록 해야할 것 같음 

## 예외 1
# 이제 내가 생각해야 하는건 뭐냐면 
# 처음에 0초에서 시작한다는 생각을 버려야 함 
# 왜냐하면 첫 요청이 언제인지 알 수 없기 때문 

## 예외 2
# 또 생각해야 하는게 뭐냐면
# 중간에 하드디스크가 유후 상태가 될 수 있음 
# 즉, 아직 모든 작업을 처리하지 않았는데 특정 시점에 대기큐가 비어서 작업을 처리할 수 없는 상태가 될 수 있음

## 첫 번째 풀이 
import heapq

maxRequireTime = 1001
def solution(jobs):
    
    priorityQueue = []
    visitedQueue = set()
    
    minRequireTime = maxRequireTime
    # 최초 실행 시간을 구해야 함 
    for jobNumber in range(len(jobs)) :
        if jobs[jobNumber][0] < minRequireTime :
            minRequireTime = jobs[jobNumber][0]
        
    
    currentTime = minRequireTime
    for jobNumber in range(len(jobs)) :
        # 요청시간, 작업의 소요시간
        requireTime, processTime = jobs[jobNumber]
        
        if requireTime == currentTime :
            heapq.heappush(priorityQueue, [processTime, jobNumber, requireTime])
            visitedQueue.add(jobNumber)
    
    returnTimes = []
    
    # 대기큐에 있다면 
    while priorityQueue :
        processTime, jobNumber, requireTime = heapq.heappop(priorityQueue)
        
        # 작업 수행 
        currentTime += processTime
        
        returnTime = currentTime - requireTime
        returnTimes.append(returnTime)
        
        # 작업이 끝난 시점에 대기큐를 갱신한다.
        # 아직 모든 작업이 대기 큐에 들어가지 않았을 때
        if len(visitedQueue) < len(jobs) :
            for jobNumber in range(len(jobs)) :
                requireTime, processTime = jobs[jobNumber]
                
                # 요청 시간이 현재 시간이거나 이전인 경우 
                if requireTime <= currentTime and jobNumber not in visitedQueue :
                    heapq.heappush(priorityQueue, [processTime, jobNumber, requireTime])
                    visitedQueue.add(jobNumber)
            
            # 작업 아직 다 못함, 근데 순회했는데 현재 시점에 대기큐가 비어 있는 경우 
            # 아직 대기큐에 들어가지 않는 작업 중 가장 요청 시간이 현재 시간과 가까운 시간을 찾아서 
            # 우선순위 큐에 넣어줘야 함 
            if not priorityQueue :
                minRequireTime = maxRequireTime
                minRequireTimeJobNumber = -1
                for jobNumber in range(len(jobs)) :
                    if jobNumber not in visitedQueue and jobs[jobNumber][0] < minRequireTime :                     
                        minRequireTime = jobs[jobNumber][0]
                        minRequireTimeJobNumber = jobNumber
                
                currentTime = minRequireTime
                requireTime, processTime = jobs[minRequireTimeJobNumber]
                heapq.heappush(priorityQueue, [processTime, minRequireTimeJobNumber, requireTime])
                visitedQueue.add(minRequireTimeJobNumber)
                

    totalReturnTime = sum(returnTimes)
    returnTimeAvg = totalReturnTime // len(returnTimes)
    
    return returnTimeAvg

# 두 번째 풀이
import heapq

def solution(jobs):
    
    newJobs = []
    
    # 데이터를 재생성한다. -> 500개 밖에 안 되기 때문에 그리 큰 시간 복잡도를 차지하지 않음 
    for jobNumber in range(len(jobs)) :
        requireTime, processTime = jobs[jobNumber] 
        
        newJobs.append([jobNumber, requireTime, processTime])
        
    sortedJob = sorted(newJobs, key=lambda x : x[1])
    
    jobCount = len(sortedJob)
    
    currentIndex = 0
    currentTime = sortedJob[0][1]
    
    priorityQueue = []
    
    returnTimes = []
    
    while len(returnTimes) < jobCount :
    
        # 현재 시간을 기준으로 들어올 수 있는 경우를 다 넣어야 함 
        while currentIndex < jobCount and currentTime >= sortedJob[currentIndex][1] :
            jobNumber, requireTime, processTime = sortedJob[currentIndex]
            heapq.heappush(priorityQueue, [processTime, jobNumber, requireTime])
            currentIndex += 1
            
        if priorityQueue :
            processTime, jobNumber, requireTime = heapq.heappop(priorityQueue)
            
            # 작업 진행 
            currentTime += processTime
            # 종료시간 - 요청시간 -> 반환 시간 구함 
            returnTime = currentTime - requireTime
            returnTimes.append(returnTime)
            
        else :
            currentTime = sortedJob[currentIndex][1]
            continue
    
    return sum(returnTimes) // len(returnTimes)