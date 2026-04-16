# 1부터 N까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있음 
# 스택에 push하는 순서는 반드시 오름차순 
# 내가 이해한 건 결국 push되는 건 반드시 오름차순 순으로 들어가야 함 
# 1 2 2 3 가능 
# 1 3 2 2 불가능 
# 내가 생각하는 건 입력값 중 가장 높은 수를 기록해놔야 함
# 가장 큰 수 보다 작은 값이 입력값으로 들어오면 그 수를 뽑아야 하거나 오름차순 정렬을 못하게 됨 
# 스택에는 가장 높은 수 + 1 ~ 입력값까지 저장하고, 결과도 따로 result로 저장해야 할 것 같음 

def solution() :
    count = int(input())

    # 마지막으로 들어간 값 
    currentNumber = 0 
    stack = []
    result = []

    for _ in range(count) :
        inputNumber = int(input())
    # 작은 값이 입력값으로 들어오면 같은 경우 그 수를 뽑아야 하거나 오름차순 정렬을 못하게 됨 
    # 이 경우는 스택을 확인해야 함 -> 스택에 값이 있어야지만 피할 수 있음 
    # 만약 스택을 확인했는데 없다면, 이건 잘못된 것임 
    # 그리고 current 값을 갱신할 필요가 없음 그 이유는 이미 최대값이 currentNumber이기 때문 
        if inputNumber <= currentNumber :

            if stack : 
                if stack[-1] == inputNumber :
                    stack.pop()
                    result.append("-")
                else :
                    print("NO")
                    return    
            else : 
                print("NO")
                return
            
        else :
            # current가 input보다 큰 경우
            for number in range(currentNumber + 1, inputNumber + 1) :
                stack.append(number)
                result.append("+")
            
            stack.pop()
            result.append("-")
            currentNumber = inputNumber

    for data in result:
        print(data)



solution()