# 앞에서 뒤로 순회하는 방법이 있음
# 단, 이 방법은 O(N**2) 시간복잡도 소요
# 이를 해결하기 위해 어떻게 해야할까 ??
# 일단 반복문을 이용해 prices를 하나씩 뽑으면서 prices의 front()와 비교하여 값이 더 작은 경우 result_table에 기록하도록 하면 어떨까 ?? 
# 그리고 만약 더 크다면 이를 스택에서 관리하도록하자, 만약 더 작은 값인 경우 스택의 peek()와 front() 값을 비교해서 값을 꺼내는 건 어떤가 ?

from collections import deque

def solution(prices):
    queue = deque(prices)
    length = len(prices)
    
    stack = []
    result_table = [0] * length
    
    for curr_index in range(length) :
        curr_price = queue.popleft()
        
        if queue and queue[0] < curr_price :
            result_table[curr_index] = curr_index + 1 - curr_index
            
            while stack and queue[0] < stack[-1][1] :
                stack_index, stack_price = stack.pop()
                result_table[stack_index] = curr_index + 1 - stack_index
        else :
            stack.append([curr_index, curr_price])
    
    while stack :
        stack_index, stack_price = stack.pop()
        result_table[stack_index] = length - 1 - stack_index
        
   
    return result_table