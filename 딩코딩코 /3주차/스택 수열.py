# push하는 순서는 반드시 오름차순을 지키도록한다.
# 임의의 수열이 주어졌을 때, 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야하는지 알아낼 수 있다 

import sys 

N = int(sys.stdin.readline().rstrip())


input_list = []
for _ in range(N):
    input_list.append(int(sys.stdin.readline().rstrip()))

def stack_sequence(input_list) -> list :

    # curr_num 변수를 0으로 초기화한다. 
    # 입력으로 들어온 데이터가 curr_num보다 크다면 curr_num + 1 부터 입력으로 들어온 데이터까지 삽입한다. 그리고 마지막 번호를 제거한다.
    # 이 때 curr_num는 마지막으로 삽입된 수를 의미한다.  

    # 입력으로 들어온 데이터가 curr_num보다 작은 경우 curr_num이 나올 때까지 pop()을 수행한다.
    # 이 때 만약, pop() 결과가 curr_num보다 작은 값이 출력되면 No 출력 

    result_list = []

    stack = []

    curr_num = 0

    for input in input_list :

        if curr_num < input : 
            
            for i in range(curr_num + 1, input + 1) :
                stack.append(i)
                result_list.append("+")

            curr_num = input
            stack.pop()
            result_list.append("-") 

        else :
            while True : 
                if not stack :
                    print("NO")
                    return -1
                
                data = stack.pop()
                result_list.append("-")

                if data == input :
                    break
                
                if data < input :
                    print("NO")
                    return -1
                

    return result_list

result = stack_sequence(input_list) 

if result != -1 :
    for i in result :
        print(i)
