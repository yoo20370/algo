# 하드디스크 한 번에 하나의 작업 수행 
# 우선순위 디스크 
## 작업이 들어왔을 때, 작업의 번호, 요청 시간, 소요 시간을 저장하는 대기큐가 있음
## 처음에는 비어있음 
### 하드 디스크 작업 X, 대기큐 비어있지 않다면, 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그작업을 시킨다. 
#### 작업 시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높음 

## 하드디스크가 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹치면, 하드디스크가 작업을 마치자마자 디스크 컨트롤러는 요청이 들어온 작업을 대기 큐 저장한 뒤 우선순위가 높은 작업을
## 작업을 대기큐에서 우선순위가 높은 작업을 대기 큐에서 꺼내서, 하드디스크에 그 작업을 시킨다. 
## 하드디스크가 어떤 작업을 마치는 시점에 다른 작업이 들어오지 않더라도 그 작업을 마치자마자 또 다른 작업을 시작할 수 있다. 
## 결국 모든 요청의 반환을 이용해 반환 평균 시간을 구해서 반환하라 !!!!

##################################  ##################################  ##################################  ##################################

# 어떻게 구현할래 ?? 
# 일단 하드디스크가 작업을 하고 있는지 아닌지 여부를 체크해야 함 -> time 변수 필요할 듯
# 작업 처리 중, 요청시간이 들어오다면 이를 우선순위 큐에 넣어준다. 이때 jobs도 우선순위 큐에 넣어서 시간을 기준으로 관리할까 ?? -> 순회하면 너무 오래 걸림 
# 매 시간마다 우선순위 큐의 요청 시간을 검사해서, 대기큐에 넣어야하는지 확인한다. (있으면 반복문 수행 - 여러 개가 요청시간이 동일한 경우가 있을 수 있음)

# 하드디스크가 특정 시간 동안 놀 수도 있잖아 ?? 
# 처음부터 5ms까지 비어있다면 -> time만 카운트해야 함 -> 조건은 뭐지 ?? require_time_heap이 존재할 떄 돌아야 함 -> 마지막 작업은 ?? -> 단순 계산으로 처리해야겠다. 
import heapq
from collections import deque

def solution(jobs):
    answer = 0
    
    require_time_heap = []
    for task_number in range(len(jobs)) :
        require_time, process_time = jobs[task_number]
        heapq.heappush(require_time_heap, (require_time, process_time, task_number))
    
    time = 0 
    # 현재 작업 중 - True, 그렇지 않으면 False
    harddisk_status = False
    
    sum_turnaround_time = 0
    
    curr_process_time = 0
    curr_require_time = 0
    curr_task_number = 0 
    curr_task_start_time = 0
    task_priority_queue = []
    
    while require_time_heap or task_priority_queue or harddisk_status:
        
        # 대기 큐에 넣을 작업 선정
        while require_time_heap and time == require_time_heap[0][0] :
            require_time, process_time, task_number = heapq.heappop(require_time_heap)
            heapq.heappush(task_priority_queue, (process_time, require_time, task_number))
        
        # 현재, 작업 중이고, 작업이 끝난 경우, 하드디스크 상태를 작업 안 하는 중으로 변경 
        if harddisk_status and curr_task_start_time + curr_process_time == time :
            # 종료 시간 - 요청 시간 
            sum_turnaround_time += (time - curr_require_time)
            harddisk_status = False
        
        # 현재, 작업중이지 않고, 대기큐에 작업이 대기하는 경우 
        if not harddisk_status and task_priority_queue:
            curr_task_start_time = time
            # 대기큐에 값이 여러개 -> 정렬해서 먼저 수행할 것 결정 
            if len(task_priority_queue) != 1 :
                task_priority_queue.sort(key = lambda x : (x[0], x[1], x[2]), reverse=True)
                
                curr_process_time, curr_require_time, curr_task_number = task_priority_queue.pop()
            else : 
                # 값이 하나면, 작업 하나에 대하여 수행 
                curr_process_time, curr_require_time, curr_task_number = task_priority_queue.pop()
                
            harddisk_status = True
        time += 1
    
    return sum_turnaround_time // len(jobs)