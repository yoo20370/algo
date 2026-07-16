# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하고자 함 
# 2개 단위로 압축 ababcdcdababcdcd -> 2ab2cd2ab2cd

# 결국 2 ~ 절반 단위로 압축해보면 될 듯
# 그리고 여기서 길이가 가장 짧은 녀석을 구하면 될 것 같음 
# 단위로 자르고 남은 문자열은 그대로 붙여줘라 

# 간단하게 생각해보면 단위로 잘라서 저장하는 것부터 하면 될 듯 
# 현재 토큰 단위를 기준으로 동일한 토큰이 몇 개인지 확인하면 될 듯 
# 만약 다음 토큰이 다른 토큰이면 다시 그 토큰 부터 오른쪽으로 순회하며 압축하면 될 듯 

# 단위로 자르는 건 결구 배열에 저장해야 하지 않나 ?? -> 순서가 유지되어야 하기 때문 
# 범위는 1 ~ length // 2 (홀/짝 모두)

# 첫 번째 문자를 기준으로 오른쪽으로 순회하면서 동일하지 않은 문자가 나올 때까지 카운트를 한다.
# 이때 기존 문자와 숫자 + 문자의 길이를 비교하여 더 짧은 것을 채택한다. 
# 그리고 동일하지 않은 문자부터 시작해서 다시 시작한다.

# 그리고 마지막 동일하지 않은 문자가 나오지 않은 경우에 대해서는 
# 동일하게 문자와 숫자 + 문자의 길이를 비교하여 더 짧은 것을 채택하도록 한다. 

from collections import deque 

def getUnitQueueList(s, length, half) :
    unitList = [deque() for i in range(half + 1)]
    
    for unit in range(1, half + 1) :
        
        startIndex = 0
        while startIndex < length :
            endIndex = startIndex + unit
            if endIndex <= length :
                unitList[unit].append(s[startIndex: endIndex])
            else : 
                unitList[unit].append(s[startIndex: ])
            
            startIndex = endIndex
    
    return unitList

def getShortString(string, pressureString) :
    pressureStringLength = len(pressureString)
    stringLength = len(string)

    if pressureStringLength < stringLength :
        return pressureString
    else :
        return string

def solution(s):
    
    # 단위로 잘라서 저장하는 것을 해야 할 듯 
    # 여기서는 2차원 배열을 사용하자 
    # [단위][잘라진 문자열 목록]
    
    length = len(s) 
    half = length // 2
    
    if length < 2 :
        return length 
    
    # 0번째 배열은 사용하지 않기 위해 1 추가
    unitQueueList = getUnitQueueList(s, length, half)
    
    
    # 압축 전혀 안 했을 때가 최대 길이임 
    minLength = length
    for unitSize in range(1, half + 1) :
        
        unitTotalString = ""
        
        currentUnitQueue = unitQueueList[unitSize]
        currentUnit = currentUnitQueue.popleft()
        
        currentUnitCount = 1
        while currentUnitQueue : 
            
            nextUnit = currentUnitQueue.popleft()
            if currentUnit == nextUnit :
                currentUnitCount += 1
                
            else : 
                
                pressureString = str(currentUnitCount) + currentUnit
                string = currentUnitCount * currentUnit
                
                shortString = getShortString(pressureString, string)
                unitTotalString += shortString
                
                currentUnit = nextUnit
                currentUnitCount = 1
        
        # 만약 끝까지 비교했는데 다른 유닛 데이터가 없거나, 비교할 데이터가 그냥 없는 경우 
        pressureString = str(currentUnitCount) + currentUnit
        string = currentUnitCount * currentUnit

        shortString = getShortString(pressureString, string)
        unitTotalString += shortString
        
        minLength = min(minLength, len(unitTotalString))
            
    return minLength