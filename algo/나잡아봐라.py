# 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝 
# 게임이 끝나는데 걸리는 최소 시간을 구하여라 

# 코니는 처음 위치 C에서 1초후 1만큼 움직임 
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# C -> 현재위치 + 1 -> 현재위치 + 2 

# 브라운은 현재 위치 B에서 다음 순간 B - 1, B + 1, 2 * B 중 하나로 움직일 수 있다.

# 그럼 1초 후에는 C는 C + 1 위치에 있고 B는 B - 1, B + 1, 2 * B 중 하나로 움직이겠네 
# 그럼 모든 경우의 수를 구하는게 맞겠군 

# 코니는 계속해서 이동하고, 브라운은 매 상황 마다 3개의 상황을 모두 수행한다.이 때 코니의 위치와 브라운의 위치가 동일하다면 빨리 끝나는 것 
# 현재 위치에서 -1, +1, * 2에 해당하는게 있다면
# 이때, 코니를 못잡는 경우가 발생할 수 있음

# 큐에 브라운의 위치를 넣는다
# (-1, +1, * 2) 세 가지 경우의 수를 계산하여 방문한 적이 없다면 큐에 삽입 
# 큐에서 꺼내고

import sys
from collections import deque

def catch_me() :
    MX = 200001

    cony_position, brown_position = map(int, sys.stdin.readline().split())

    graph = [{} for _ in range(MX)]

    queue = deque()
    queue.append([brown_position,0])
    graph[brown_position][0] = 1

    # 코니 위치를 while 문에서 체크할거잖아 ?? 그치 그러면 언제를 기준으로 할거야 -> 아무것도 하기 전, 값을 증가시킨다음에 하는 것 
    # cony_position < MX 는 증가한 후의 이야기 

    # 증가한 후로 체크를 하고 처음부터 확인을 하는거지 처음에는 0이 증가했다고 가정 
    # 큐에서 꺼낸 값을 비교하는게 맞지 않나 ?? 

    value = 0
    while cony_position < MX :
        
        for _ in range(0, len(queue)) : 
            curr_brown_position, curr_value = queue.popleft()
            
            # 위치 비교 
            if cony_position == curr_brown_position :
                return value

            result = curr_brown_position - 1
            # 범위 내에 있는가 ? 그리고 방문한 적이 있는가 ?? (가장 먼저 방문한 것이 가장 짧은 거리를 가지므로 갱시해줄 필요가 없음)
            if result >= 0 and result < MX and value + 1 not in graph[result]:
                graph[result][value + 1] = True
                queue.append([result, value + 1])
                
            result = curr_brown_position + 1
            if result >= 0 and result < MX and value + 1 not in graph[result]:
                graph[result][value + 1] = True
                queue.append([result, value + 1])

            result = curr_brown_position * 2
            if result >= 0 and result < MX and value + 1 not in graph[result]:
                graph[result][value + 1] = True
                queue.append([result, value + 1])

        value += 1
        cony_position += value
    # 끝까지 못잡은 경우
    return value

print(catch_me())
    