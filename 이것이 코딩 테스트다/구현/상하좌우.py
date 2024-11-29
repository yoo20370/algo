import sys

N = int(sys.stdin.readline().rstrip())

commands = sys.stdin.readline().split()

x = 1
y = 1
for command in commands :  
    if command == "L" and x - 1 != 0 :
        x -= 1 
    elif command == "R" and x + 1 != N + 1:
        x += 1

    elif command == "U" and y - 1 != 0 :
        y -= 1
    
    elif command == "D" and y + 1 != N + 1 :
        y += 1
    
print(y, x)


