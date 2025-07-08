# N개의 수로 이루저진 수열 A1 A2 ... An이 주어진다. 
# 수와 수 사이에 끼워 넣을 수 있는 N - 1개의 연산자가 주어진다. 
# 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다. 

## 완전 탐색 아닌가 ?? 
## 모든 경우의 수를 고려해서 최대값과 최소값을 구하면 되는거 아닌가 ?? 

### 어떻게 만들어야할까 
### BFS를 이용해서 첫 원소에 대하여 모든 경우의 수를 고려한 결과값을 큐에 넣는다. (이때, 개수를 감소 시킨 형태로 전달한다.)
### 큐에서 꺼낸 값을 대상으로 동일한 방식을 취한다. 
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