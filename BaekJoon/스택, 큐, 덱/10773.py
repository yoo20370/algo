import sys

N = int(sys.stdin.readline().rstrip())


stack = list()
for i in range(N) :
    data = int(sys.stdin.readline().rstrip())
    
    if data != 0 :
        stack.append(data)
    else :
        stack.pop()

print(sum(stack))