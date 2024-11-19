import sys

def check(string) :

    stack = list()
    for i in string :
        if i == "(" :
            stack.append("(")
        elif i == "[" :
            stack.append("[")
        elif i == ")" :
            if len(stack) != 0 and stack[len(stack) -1] == "(":
                stack.pop()
            else :
                return "no"
        elif i == "]" :
            if len(stack) != 0 and stack[len(stack) -1] == "[":
                stack.pop()
            else :
                return "no"
    
    if len(stack) != 0 :
        return "no"
    else :
        return "yes"
            

while True :
    data = sys.stdin.readline().rstrip()
    if data == "." :    
        break

    print(check(data))
            

