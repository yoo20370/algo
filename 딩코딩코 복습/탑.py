import sys

def top(n, topList) -> list:

    # 마지막 원소를 꺼낸다.
    # 마지막 원소가 topList의 top과 비교한다.
    # 마지막 원소가 더 크다면 stack에 넣고 ([인덱스, 높이])
    # 마지막 원소가 더 작다면 결과 테이블에 기록한다.
    # 또한 스택에서 pop()하여 비교하고 더 작다면 기록한다. (작은 원소가 나올 때까지)
    result_table = [0] * n

    stack = []
    while topList :
        curr_idx = len(top_list) - 1
        curr_height = topList.pop()

        if top_list and top_list[-1] > curr_height :
            result_table[curr_idx] = len(top_list)

            while stack and top_list[-1] > stack[-1][1] :
                last_index, last_height = stack.pop() 
                result_table[last_index] = len(top_list)
        else :
            stack.append([curr_idx, curr_height])

    return result_table

n = int(sys.stdin.readline().rstrip())

top_list = list(map(int, sys.stdin.readline().split()))

for i in top(n, top_list) :
    print(i, end=" ")

                
        
top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    stack = []  # [인덱스, 높이]를 저장
    answer = [0] * len(heights)
    
    for i in range(len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1][0] + 1
        stack.append([i, heights[i]])
    
    return answer