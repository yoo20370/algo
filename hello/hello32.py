# 커리큘럼 

# 동시에 여러 개의 강의를 들을 수 있음 
# 결국 선수 과목을 들어야 현재 과목을 들을 수 있고, 선수과목 중 가장 시간이 긴 과목을 들어야지만 
# 현재 과목을 들을 수 있는 거 아닌가 ? 

# 그렇다는 건 결국 진입차수가 0이 되는 순간에 가용치를 기록하면 되는거 아닌가 ? 

import sys, heapq

def solution() :

    courseCount = int(sys.stdin.readline().rstrip())

    # 각 강의의 시간 
    courseTimes = [0] * (courseCount + 1)

    # 강의를 수강하기까지 최소 시간 
    waitTimes = [0] * (courseCount + 1)

    # 선수 과목 목록 
    preSubjects = [[] for _ in range(courseCount + 1)]

    entryDegree = [0] * (courseCount + 1)

    maxWaitTimes = [0] * (courseCount + 1)

    # 강의 시간, 강의를 듣기 위한 선수 과목
    for number in range(1, courseCount + 1) :

        inputList = list(map(int, sys.stdin.readline().split()))

        # 강의 시간 기록 
        courseTimes[number] = inputList[0]

        for index in range(1, len(inputList) - 1) :
            
            # 진입 차수 증가 
            # number가 목적지
            # -1이 아닌 값이 출발지 
            entryDegree[number] += 1

            subject = inputList[index]  
            # 출발지에서 도착지로 가는 걸 기록해야 함 -> 그래야 출발지 노드에 도달 했을 때 간선을 지우면서 진입 차수를 낮출 수 있음 
            # 여기서 subject가 선수 과목 (출발지)
            # number가 이수 과목 (목적지)
            preSubjects[subject].append(number)

    priorityQueue = []

    # 진입차수가 0인 과목 즉, 바로들을 수 있는 과목을 넣는다.
    for index in range(1, len(entryDegree)) :
        if entryDegree[index] == 0 :
            heapq.heappush(priorityQueue, index)

    
    while priorityQueue :
        # 수강 강의 
        courseNumber= heapq.heappop(priorityQueue)

        # 내 강의를 들을 수 있으니 선수 과목 중 가장 긴 과목의 대기 시간 + 내 과목 시간 
        waitTimes[courseNumber] = maxWaitTimes[courseNumber] + courseTimes[courseNumber]

        for adjacentCourse in preSubjects[courseNumber] :
            entryDegree[adjacentCourse] -= 1

            # 선수 과목 중 더 큰 값을 기록하도록 함 (선수 과목 여러 개인 경우 대기 시간 중 가장 큰 값을 가지고 있게 함)
            maxWaitTimes[adjacentCourse] = max(maxWaitTimes[adjacentCourse], waitTimes[courseNumber])
            
            if entryDegree[adjacentCourse] == 0 :
                heapq.heappush(priorityQueue, adjacentCourse)
                

        
    # 이제 생각해야 하는게 선수 과목 중에 가장 대기 시간이 긴 과목을 어떻게 찾아서 기록할 것인가 ?? 
    # 가장 쉬운 방법은 이수 과목의 선수 과목 최대값을 따로 관리하는 것 
    # 즉, 현재 과목을 수강할 때, 이제 이수과목으로 가는 진입 차수가 1씩 제거되는데 이 때 인접한 노드들에 대해서 heap에 넣을 때, 최대값을 넣어서 관리해버리는 것 
    # 인접한 노드를 순회하는데 이때, 최대값을 구하자는 뜻 
    # 그리고 현재 과목을 수강할 때, 즉 queue에서 꺼내져 로직이 실행될 때, 대기 시간에 추가하면 되지 않나 ?? 

    # 다른 방법 없나 ?? 
    # 우선순위 큐에 (들을 강의, 이 강의를 들을 때까지 걸린 시간) 
    # 과목을 듣게 되면, 강의, 걸린 시간을 꺼낸다.
    # 강의를 듣는데 걸린 시간을 기록한다. 
    # 인접한 강의를 순회하면서 진입 차수를 줄인다.
    # 지금까지 걸린 시간과 기존 걸린 시간 중 큰 값을 기록한다. (여러 선수 강의가 있는 경우 이 과정을 반복 하고 최종적으로 가장 높은 시간이 기록됨) 

    print(waitTimes)



solution()