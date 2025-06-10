from collections import deque

# 브라운이 코를 잡거나, 코니가 너무 멀리 달아나면 끝 
# 게임이 끝나는데 최소시간을 구하라
# 코니는 C에서 1초후 1만큼 움직인다. 
# 가속이 붙어서 이전 이동 거리 + 1
# 1, 2, 3, 4

# 브라운은 B - 1, B + 1, B * 2

# 코니는 이동할 위치가 정해져 있다. 
# 브라운은 상황에 따라서 다르게 이동해야 한다.
# 언제 B - 1, 언제 B + 1을 하고

def catch_me(cony_position, brown_position) -> int:

    # 코니의 위치는 고정되어 있으므로 단순히 계산만 한다.
    # 브라운 세 가지 이동을 코니의 위치에 따라 계속 계산한다. 
    # 예를 들어 코니가 12일 때, 브라운 3위치에 대하여 BFS를 수행하여 모든 경우의 수를 구한다. 

    # 큐에 위치 넣어야 함
    # 언제 위치를 넣어야하지 ?? 
    # 이동한 위치를 넣을 것인가 아니면 이동하기 전 위치를 넣을 것이냐
    # 이동한 위치를 넣는게 맞다고 생각 

    queue = deque()
    queue.append(brown_position)

    time = 0
    while cony_position <= 200000 :
        visited = set()
        while queue :
            curr_position = queue.popleft()
    
            # 현재 시간
            if curr_position == cony_position :
                return time
            
            else :
                # 다음 시간에 비교할 위치를 큐에 적재 
                if curr_position - 1 >= 0 and curr_position - 1 not in visited :
                    visited.add(curr_position - 1)
                
                if curr_position + 1 <= 200000 and curr_position + 1 not in visited :
                    visited.add(curr_position + 1)

                if curr_position * 2 <= 200000 and curr_position * 2 not in visited:
                    visited.add(curr_position * 2)

        queue.extend(list(visited))
        time += 1
        cony_position += time

    return time

print("정답 = 0 / 현재 풀이 값 = ", catch_me(0,0))
print("정답 = 5 / 현재 풀이 값 = ", catch_me(11,2))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))

    
    
    

    
