# 문자열 뒤집기 
# 0과 1로 구성 
# 문자열을 모두 같은 문자로 바꾸고자 함 
# 연속된 숫자는 한 번에 뒤집을 수 있음 

# 0001100 
# 1111111 입장에서 시작 000은 111로 변경해야 하는 부분 
# 0000000 입장에서는 변경할 필요가 없음 

# 순회하면서 0에서 1로 변하는 것
## 0000000 입장에서 0으로 변경해야 하는 부분 
## 1111111 입장에서는 변경할 필요가 없는 부분 

# 순회하면서 1에서 0으로 변하는 것 
## 0000000 입장에서는 변경할 필요가 없는 부분 
## 1111111 입장에서 0으로 변경해야 하는 부분 

# 코드 설계를 하자면 결국
# 처음 시작하는 값이 무엇인지에 따라 카운트 
# 숫자가 바뀌는 지점에서 카운트 

ZEROCHAR = '0'

def solution() :
    string = input()
    length = len(string)

    # 1 -> 0
    changeZeroCount = 0

    # 0 -> 1
    changeOneCount = 0

    
    currentChar = string[0]
    if currentChar == ZEROCHAR : 
        changeOneCount = 1
    else : 
        changeZeroCount = 1

    
    for index in range(1, length) :
        nextChar = string[index]
        if currentChar != nextChar : 
            if nextChar == ZEROCHAR :
                changeOneCount += 1
                
            else :
                changeZeroCount += 1
            
            currentChar = nextChar
        
    return min(changeOneCount, changeZeroCount)


result = solution()
print(result)