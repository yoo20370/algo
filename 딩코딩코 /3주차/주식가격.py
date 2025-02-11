from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))] 
    
    # prices를 큐에 삽입한다.
    # stack이 비어있는 경우 스택에 price에서 꺼내서 본인 인덱스와 price를 저장한다.
    # 비어있지 않은 경우, prices의 맨 앞 값과 스택의 맨 위 price 값을 비교한다.
    # 큐의 맨 앞이 더 작다면 answer[스택_index] = 큐_index - 스택_index
    # 큐의 맨 앞이 더 크다면 꺼내서 스택에 삽입한다.
    # 만약 큐가 모두 비어버리면, 전체 길이 - 1 - 본인_index 값을 answer에 저장한다.
    total_prices_length = len(prices)
    queue = deque(prices)
    stack = []
    queue_index = 0
    
    while queue :
        queue_price = queue[0]
        
        if stack and queue_price < stack[-1][1] :
            stack_index, stack_price = stack.pop()
            answer[stack_index] = queue_index - stack_index
            continue 
        
        stack.append((queue_index, queue.popleft()))
        queue_index += 1
    
    while stack : 
        stack_index, stack_price = stack.pop()
        answer[stack_index] = total_prices_length - stack_index - 1
        
    return answer