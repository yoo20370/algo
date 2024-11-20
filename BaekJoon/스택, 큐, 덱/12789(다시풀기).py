# 문제를 잘못 이해해서 틀린 것 같음 
# import sys
# from collections import deque

# N = int(sys.stdin.readline().rstrip())


# def dokey(n) :
#     dequeue = deque(map(int, sys.stdin.readline().split()))
#     stack = list()

#     stackPassNum = n + 1
#     passNum = 1 
#     while passNum != n + 1 :
#         if len(stack) > 0 and stack[len(stack) -1] == passNum :
#             # 스택에서 꺼내 통과시킬 수 있는 경우 통과 시킨다.
#             stack.pop()
#             passNum += 1
#             if len(stack) > 0 :
#                 stackPassNum = stack[len(stack) - 1]
#             else :
#                 stackPassNum = n + 1
#         elif len(dequeue) == 0 :
#             return "Sad"
        
#         if len(dequeue) > 0 :
#             data = dequeue.popleft()
#             if data == passNum :
#                 passNum += 1
#             elif stackPassNum > data :
#                 stack.append(data)
#                 stackPassNum = data 
#             else : 
#                 return "Sad"
        
#     return "Nice"

# print(dokey(N))

# 정답 코드 
# def dokey(n):
#     dequeue = deque(map(int, sys.stdin.readline().split()))
#     stack = []
#     passNum = 1

#     while dequeue or stack:
#         if dequeue and dequeue[0] == passNum:
#             dequeue.popleft()
#             passNum += 1
#         elif stack and stack[-1] == passNum:
#             stack.pop()
#             passNum += 1
#         elif dequeue:
#             stack.append(dequeue.popleft())
#         else:
#             return "Sad"

#     return "Nice"

import sys
from collections import deque

def check() :
    N = int(sys.stdin.readline().rstrip())
    dequeue = deque(map(int, sys.stdin.readline().split()))
    stack = list()

    passNum = 1
    while dequeue or stack :
        
        if dequeue and dequeue[0] == passNum :
            dequeue.popleft()
            passNum += 1
        elif stack and stack[len(stack) -1] == passNum :
            stack.pop()
            passNum += 1
        elif dequeue :
            data = dequeue.popleft()
            stack.append(data)
        else :
            return "Sad"
    return "Nice"


print(check())