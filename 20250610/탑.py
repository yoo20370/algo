# 결과를 저장할 결과 테이블이 필요 -> 0으로 초기화 
# 첫 번째 반복문에서는 모든 탑을 순회하는데 뒤에 탑부터 앞으로 순회한다.
# 순회하면서 값을 뽑고, top_list 스택의 peek()와 비교하여 만약 peek()가 더 크다면 현재 인덱스를 결과 테이블에 기록하고, 스택의 peek()와 비교한다. 스택의 peek()보다 크다면 스택에 대한 결과 테이블을 저장하고 이를 반복
# 반대로 작다면 아무것도 수행하지 않는다. 

import sys

def top(top_count, top_list) :
    
    result_table = [0] * top_count
    stack = []

    # O(top_count)
    for curr_index in range(top_count - 1, -1, -1) :
        curr_height = top_list.pop()

        if top_list and top_list[-1] > curr_height :
            result_table[curr_index] = len(top_list)

            while stack :
                if top_list[-1] > stack[-1][1] :
                    curr_index, curr_height = stack.pop()
                    result_table[curr_index] = len(top_list)
                else :
                    break

        else :
            stack.append((curr_index, curr_height))
    
    return result_table

top_count = int(sys.stdin.readline().rstrip())
top_list = list(map(int, sys.stdin.readline().split()))

for i in top(top_count, top_list) :
    print(i, end=" ")
        

