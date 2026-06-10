from collections import deque

def catch_me(cony_position, brown_position) -> int:

    queue = deque()
    queue.append(brown_position)

    time = 0
    while cony_position <= 200000 :
        visited = set()
        while queue :
            curr_position = queue.popleft()
    
            if curr_position == cony_position :
                return time
            
            else :
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

    
    
    

    
