import sys
from collections import deque 

input = sys.stdin.readline

def solution() :
    number_count = int(input().rstrip())

    number_list = list(map(int, input().split()))
    operator_list = list(map(int, input().split()))

    # (현재 합, 인덱스, 연산자_리스트) 형태로 큐에 넣자
    queue = deque()
    queue.append((number_list[0], 1, operator_list))

    min_sum = int(1e10)
    max_sum = -int(1e10)
    
    while queue : 
        curr_sum, curr_index, curr_operator_list = queue.popleft() 
        
        a, b, c, d = curr_operator_list
        if curr_index < number_count :
            if a != 0 :
                result_sum = curr_sum + number_list[curr_index]
                queue.append((result_sum, curr_index + 1, [a - 1, b, c, d]))
           
            if b != 0 :
                result_sum = curr_sum - number_list[curr_index]
                queue.append((result_sum, curr_index + 1, [a, b - 1, c, d])) 
              
            if c != 0 :
                result_sum = curr_sum * number_list[curr_index]
                queue.append((result_sum, curr_index + 1, [a, b, c - 1, d]))
                
            if d != 0:
                next_number = number_list[curr_index]
                if curr_sum < 0:
                    result_sum = -(-curr_sum // next_number)
                else:
                    result_sum = curr_sum // next_number
                queue.append((result_sum, curr_index + 1, [a, b, c, d - 1]))
               

        else :
            min_sum = min(min_sum, curr_sum)
            max_sum = max(max_sum, curr_sum)

    print(max_sum)
    print(min_sum)

solution()