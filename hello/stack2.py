
import sys

def solution() :

    n = int(sys.stdin.readline().rstrip())

    result = []

    stack = []

    nextPushNumber = 1
    for _ in range(n) :

        inputNumber = int(sys.stdin.readline().rstrip())

        if nextPushNumber <= inputNumber :
            for number in range(nextPushNumber, inputNumber + 1, 1) :
                result.append("+")
                stack.append(number)
            
            result.append("-")
            stack.pop()

            nextPushNumber = inputNumber + 1
        
        else:
            if stack and stack[-1] == inputNumber :
                result.append("-")
                stack.pop()

            else : 
                print("NO")
                return 

    for char in result :
        print(char)

solution()
