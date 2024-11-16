import sys 

N = int(sys.stdin.readline().rstrip())

stack = list()
for i in range(N) :
    data = sys.stdin.readline().rstrip()
    if len(data) != 1 :
        x, y = map(int, data.split())
    else :
        x = int(data)
    
    if x == 1 :
        stack.append(y)
    elif x == 2 :
        if len(stack) == 0 :
            print(-1)
        else : 
            print(stack.pop())
    elif x == 3 :
        print(len(stack))
    elif x == 4 :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif x == 5 :
        if len(stack) != 0 :
            print(stack[len(stack)-1])
        else :
            print(-1)
    


