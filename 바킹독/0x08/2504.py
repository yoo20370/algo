import sys
from collections import deque

input_data = deque(sys.stdin.readline().rstrip())
    
def check(input_data) -> int :

    stack = list()

    val = 0
    while input_data :
        char = input_data.popleft()

        if char == '(' :
            stack.append('(')

        elif char == '[' :
            stack.append('[')
        elif char == ')' :
            # 스택이 비어있거나 일치하지 않는 괄호인 경우 0을 반환하여 끝내면 됨 
            if len(stack) == 0 or stack[-1] == '[' :
                return 0

            data = stack.pop() 
            # 닫는 괄호가 등장했을 때, 스택에서 꺼낸 값이 일치하는 여는 괄호일 경우 가지고 있던 수와 곱한 후 다시 스택에 넣는다.
            if data == '(' :
                if val == 0 :
                    result = 2 
                else : 
                    result = val * 2 
                stack.append(result)
                val = 0
            else : 
                 # 닫는 괄호가 등장했을 떄, 스택에서 꺼낸 값이 숫자인 경우 스택에서 해당 숫자를 꺼내 가지고 있는다. 
                input_data.appendleft(')')
                val += data

        elif char == ']' :
            if len(stack) == 0 or stack[-1] == '(' :
                return 0

            data = stack.pop() 

            # 닫는 괄호가 등장했을 때, 스택에서 꺼낸 값이 일치하는 여는 괄호일 경우 가지고 있던 수와 곱한 후 다시 스택에 넣는다.
            if data == '[' :
                if val == 0 :
                    result = 3 
                else : 
                    result = val * 3

                stack.append(result)
                val = 0
            else : 
                 # 닫는 괄호가 등장했을 떄, 스택에서 꺼낸 값이 숫자인 경우 스택에서 해당 숫자를 꺼내 가지고 있는다. 
                input_data.appendleft(']')
                val += data
    try :
        result = sum(stack)
    except Exception:
        return 0
    return result

print(check(input_data))

# bracket = list(input())
# stack = []
# answer = 0
# tmp = 1

# for i in range(len(bracket)):

#     if bracket[i] == "(":
#         stack.append(bracket[i])
#         tmp *= 2

#     elif bracket[i] == "[":
#         stack.append(bracket[i])
#         tmp *= 3

#     elif bracket[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0
#             break
#         if bracket[i - 1] == "(":
#             answer += tmp
#         stack.pop()
#         tmp //= 2

#     else:
#         if not stack or stack[-1] == "(":
#             answer = 0
#             break
#         if bracket[i-1] == "[":
#             answer += tmp

#         stack.pop()
#         tmp //= 3

# if stack:
#     print(0)
# else:
#     print(answer)
