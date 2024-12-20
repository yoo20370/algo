import sys

def check(string) -> str :
    
    stack = list()

    for char in string :
        if char == '(' :
            stack.append('(')
        elif char == '[' :
            stack.append('[')
        elif char == ')' :
            if len(stack) == 0 or stack[-1] != '(' :
                return "no"
            else :
                stack.pop()
        elif char == ']' :
            if len(stack) == 0 or stack[-1] == '(' :
                return "no"
            else :
                stack.pop()
    
    if len(stack) != 0 :
        return "no"

    return "yes"

result = list()
strings = list()
while True :
    input_data = sys.stdin.readline().rstrip()
    if len(input_data) == 1 and input_data[0] == '.' :
        break
    print(check(input_data))



