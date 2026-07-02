# 접근 자체를 잘못한 듯 
# 두 색이 개수가 같은 경우 ??

# 2 * 1 
# 1 
# 24 -> 2 12 - 
# 24 -> 6 4 - 24 
# 24 -> 24 1 


# 결국 노랑 개수가 홀수인지 짝수인지에 다르게 처리할 필요 없을 듯 
# 짝수라면 약수 구해서 모두 확인하면 될 듯
# 노랑의 약수를 구해야 함 
# 2 -> 1과 2 

# 약수 구하기.....
# 어떻게 하더라 ?? ㅋㅋㅋㅋㅋㅋ

# 내가 약수를 어떻게 구했더라 ?? 
# 24의 약수는 ?? -> 하나 하나 확인해가면서 나누어 떨어지는지 확인했음 
# 그렇게 한다고 하면 ?? 근데 이걸 다 할 필요 없이 제곱근 까지만 하면 됨 
# 그렇게 구해서 반환하도록 해보자 

# 이때 문제가 노랑 개수가 홀수라는게 문제임 
# (세로 개수 + 2) * (가로 게수 + 2) - 노랑 개수 = 갈색 개수 

# 결국 특정 값의 약수를 구해서 크기를 정해야할 듯 이때, 곱의 두 수에 대해서 처리하면 되므로 
# 제곱근 + 1까지만 확인하면 될듯 

def getMeasureNumber(number) :
    result = [1]
    
    for i in range(2, int(number**0.5) + 1) :
        if number % i == 0 :
            result.append(i)
            
    return result

def equals(brownCount, yellowCount, number) : 
    
    temp = yellowCount // number 
    
    calculateBrownCount = (temp + 2) * (number + 2) - yellowCount
    
    if brownCount == calculateBrownCount :
        return True
    
    return False

def solution(brown, yellow):
    
    mesureNumberList = getMeasureNumber(yellow)
    
    
    for number in mesureNumberList :
        row = col = 0
        if equals(brown, yellow, number) :
            temp = yellow // number 
            col = max(number, temp)    
            row = min(number, temp)
            
            return [col + 2, row + 2]
            
        