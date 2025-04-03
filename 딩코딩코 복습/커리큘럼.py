# 위상 정렬을 이용해서 푼다.
# 단, 동시에 강의를 들을 수 있기 때문에 동시에 듣는 강의 중 더 오래 걸리는 값으로 수강 시간을 갱신한다. 
from collections import deque
import sys

def topo_sort() -> None :
    lecture_cnt = int(sys.stdin.readline().rstrip())

    entry_list = [0 for _ in range(lecture_cnt + 1)]
    time_list = [0 for _ in range(lecture_cnt + 1)]
    max_time = [0 for _ in range(lecture_cnt + 1)]
    graph = [[] for _ in range(lecture_cnt + 1)]

    for i in range(1, lecture_cnt + 1) :
        data = list(map(int, sys.stdin.readline().split()))

        time_list[i] = data[0]
        for curr_data in [data[idx] for idx in range(1, len(data)) if data[idx] != -1] :
            entry_list[i] += 1
            graph[curr_data].append(i)

    # 어떻게 처리할 것인가 ?? 
    # 큐에 진입차수가 0인 강의을 먼저 넣는다. 
    # 큐에서 강의를 하나 꺼내 듣는다. 
    # 해당 강의를 듣고 나서 들을 수 있는 강의의 진입 차수를 제거한다.
    # 만약 진입차수가 0이라면 큐에 넣고, max_time 값을 time_list에 추가한다. 
    # 그렇지 않은 경우 max_time에 시간을 기록한다.(시간이 긴 강의가 먼저 들을 수 있기 때문)
    # 큐가 빌 때까지 이를 반복한다.

    queue = deque()
    for i in range(1, lecture_cnt +1) :
        if entry_list[i] == 0 :
            queue.append(i)

    while queue :
        curr_lecture = queue.popleft()

        for next_lecture in graph[curr_lecture] :
            entry_list[next_lecture] -= 1

            # 선수 과목 중 가장 긴 과목의 시간을 찾기 위함 
            if max_time[next_lecture] < time_list[curr_lecture] :
                max_time[next_lecture] = time_list[curr_lecture]
            
            if entry_list[next_lecture] <= 0 :
                time_list[next_lecture] += max_time[next_lecture]
                queue.append(next_lecture)
    
    print(time_list)
            
    
topo_sort()