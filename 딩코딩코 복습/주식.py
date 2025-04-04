# prices가 빌 때까지 반복한다.
# prices에서 leftpop()을 수행하여 curr_number에 저장, current_index도 저장 
# prices가 비어있지 않다면 맨 앞의 원소와 현재 원소를 비교한다. 만약 현재 원소가 작다면 맨 앞 인덱스 - 본인 인덱스를 결과 테이블에 저장 
# 스택의 top 값이랑 비교하여 prices 맨 앞 원소가 더 작다면, 본인 인덱스 결과 테이블에 저장
# 그것이 아니라면 다음 과정 수행 
# 현재 원소가 더 크다면 스택에 삽입 
from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    total_length = len(prices)
    
    queue = deque(prices)
    stack = []
    
    curr_index = 0
    while queue :
        curr_price = queue.popleft()
        
        if queue and curr_price > queue[0] :
            answer[curr_index] = total_length - len(queue) - curr_index
            
            while stack and stack[-1][1] > queue[0] :
                last_index, last_price = stack.pop()
                answer[last_index] = total_length - len(queue) - last_index
        else :
            stack.append([curr_index, curr_price])
        
        curr_index += 1
    
    while stack :
        last_index, last_price = stack.pop()
        answer[last_index] = curr_index - last_index - 1
        
    return answer