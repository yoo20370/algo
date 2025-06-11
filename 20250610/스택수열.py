import sys

# 입력값이 들어오면 해당 입력값 숫자까지 스택에 삽입한다. 
# 마지막에 저장한 값은 제거한다. 
# 이때, 입력값이 peek()값과 동일하면 문제가 없음 
# 그렇지 않고 다른 값이 존재하면 에러 

def stack_number_sequence() :

    input_count = int(sys.stdin.readline().rstrip())
    result_string = []

    stack = []
    next_number = 1
    for _ in range(input_count) :
        
        input_number = int(sys.stdin.readline().rstrip())

        if input_number < next_number and stack :
            if stack[-1] == input_number :
                stack.pop()
                result_string.append("-")
                continue
            else :
                print("NO")
                return 
            
        for number in range(next_number, input_number + 1) :        
            stack.append(number)
            result_string.append("+")
            next_number = input_number + 1

        stack.pop()
        result_string.append("-")

    for i in result_string :
        print(i)
    return 0

stack_number_sequence()



