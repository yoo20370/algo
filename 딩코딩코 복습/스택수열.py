# 스택이 비어있지 않다면, 스택에 top 원소의 값보다 현재 들어온 값이 더 작다면 NO를 출력하고 함수를 종료한다.
# 이전에 들어온 값보다 현재 들어온 값이 가장 큰 값보다  더 크다면 이전에 들어온 값 + ~ 현재 들어온 값까지 스택에 삽입한다.
# 스택에서 마지막 원소를 꺼내서 이전에 들어온 값으로 기록한다. 

import sys

def stack_sequence(n) -> None :
    result_list = []
    stack = []

    before_number = 0
    for _ in range(n) :
        curr_number = int(sys.stdin.readline().rstrip())

        if stack and stack[-1] > curr_number :
            print("NO")
            return
        
        for i in range(before_number + 1, curr_number + 1) :
            stack.append(i)
            result_list.append("+")
        
        before_number = max(before_number, stack.pop())
        result_list.append("-")

    for i in result_list :
        print(i)

n = int(sys.stdin.readline().rstrip())

stack_sequence(n)




