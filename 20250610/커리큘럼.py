import sys
from collections import deque

# 자 생각을 해봅시다. 
# 내가 1번 강의를 들으면 2번 3번 강의를 들을 수 있게 됨 -> 1번 강의를 들었을 때, 2번, 3번, 4번 진입 차수를 1씩 감소시켜줘야 함 
# 강의 시간을 어떻게 처리해줘야 할까 ?? 

# 처음에 진입차수가 0인 데이터를 큐에 저장할 때, result_times 본인의 강의 시간을 기록한다. (선수과목이 없으므로 그냥 기록)
# 큐에서 꺼내서 진입 차수를 차례로 제거할 때 result_times[선수과목] + 현재 강의 시간이랑 result_times[현재과목] 중 max 값을 result_times에 저장한다. 
def corriculum() :

    lecture_count = int(sys.stdin.readline().rstrip())
    lecture_times = [0] * (lecture_count + 1)

    # graph 안에 번호에 해당하는 강의를 들어야 함 
    graph = [[] for _ in range(lecture_count + 1)]

    # 진입 차수
    entry_counts = [0] * (lecture_count + 1)
    for index in range(1, lecture_count + 1) :
        input_data = list(map(int, sys.stdin.readline().split()))
        
        # 강의 시간 
        lecture_times[index] = input_data[0]
        
        for node in input_data[1:-1] :
            graph[node].append(index)
            entry_counts[index] += 1

    # 시간 기록을 위한 테이블 
    result_times = [0] * (lecture_count + 1)
    queue = deque()

    for lecture_number in range(1, lecture_count + 1) :
        if entry_counts[lecture_number] == 0 :
            queue.append(lecture_number)
            result_times[lecture_number] = lecture_times[lecture_number]

    while queue : 
        curr_lecture = queue.popleft()

        for next_lecture in graph[curr_lecture] :
            entry_counts[next_lecture] -= 1
            # 선수 과목 걸린 시간 + 현재 과목 시간, 이전에 기록된 결과와 비교해서 max 값을 다시 저장 
            result_times[next_lecture] = max(result_times[curr_lecture] + lecture_times[next_lecture], result_times[next_lecture]) 

            # 진입 차수가 0이라면 큐에 넣는다. 
            if entry_counts[next_lecture] == 0 :
                queue.append(next_lecture)


    for index in range(1, len(result_times)) :
        print(result_times[index])

corriculum()