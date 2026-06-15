# 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오 

# 코니는 처음 위치 C에서 1초 후 1만큼 움직인다. 
# 이후에는 가속이 붙어 매초마다 이전 이동 거리 + 1 만큼 움직인다. 

# C, C + 1, C + 1 + 2(이동 거리), C + 3 + 3(이동 거리) ... 

# 브라운은 현재 위치 B에서 B - 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다. 

# 초당 경우 코니의 위치 - 고정 
# 초당 브라운의 위치 (모든 경우의 수)

# 결국, 초를 기준으로 코니와 브라운의 위치를 계산해야 함 이때, 코니는 위치가 초당 고정이기 떄문에 고려할 필요가 없지만
# 브라운은 경우의 수가 3가지 이므로, 모든 가능한 경우를 고려해야 함 
# bfs로 가자 인접한 경우를 고려하는 것이기 때문

# 현재 코니 위치를 구한다.
# 현재 브라운 위치를 구한다.

from collections import deque

c = 11
b = 2

def catch_me(cony_loc, brown_loc):

    if cony_loc == brown_loc :
        return 0

    currentSpeed = 0 
    currentSecond = 0 

    # (코니 위치, 브라운 위치, 초단위)
    queue = deque([[brown_loc, 0]])

    visited = set()
    visited.add((brown_loc, 0))

    while cony_loc <= 200000 :

        cony_loc += currentSpeed

        # 현재 코니의 위치를 구하기 위해 이전 코니의 위치를 꺼내야 한다.
        # 바로 큐에 넣으면 무한 루프에 빠지지 않을까 ?? 
        # 그럼 꺼내기 전에 시간을 고려해야 하나 ?? 
        # 어짜피 큐에는 시간 순으로 들어가기 때문에 그렇게 해도 될 것 같음 
        
        while queue and queue[0][1] == currentSecond - 1 :
            beforeBrownLocation, beforeSecond = queue.popleft()

            # case1, 2, 3은 현재 시간의 가능한 경우들을 의미하는 것임 
            case1 = beforeBrownLocation - 1
            if case1 >= 0 and case1 <= 200000 :
                if case1 == cony_loc :
                    return currentSecond
                
                if (case1, currentSecond) not in visited : 
                    queue.append((case1, currentSecond))
                    visited.add((case1, currentSecond))
                

            case2 = beforeBrownLocation + 1 
            if case2 >= 0 and case2 <= 200000 :
                if case2 == cony_loc :
                    return currentSecond
                
                if (case2, currentSecond) not in visited : 
                    queue.append((case2, currentSecond))
                    visited.add((case2, currentSecond))

            case3 = beforeBrownLocation * 2
            if case3 >= 0 and case3 <= 200000 :
                if case3 == cony_loc :
                    return currentSecond
                
                if (case3, currentSecond) not in visited : 
                    queue.append((case3, currentSecond))
                    visited.add((case3, currentSecond))

        currentSpeed += 1
        currentSecond += 1
        

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))