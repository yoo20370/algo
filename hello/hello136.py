# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
##   단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.

# 재귀가 필요할 것 같음 
# 문자열 W에 대해서 균형잡힌 문자열을 가져와야 함 

# 1
# u = ()
# v = ))((()

# 2
# u = ))((
# v = ()

# u가 올바른 문자열이 아님 
# 다음 단계 수행 

# w = ()
# u = ()
# v = ""

# 새로운 문자열 = "(())()"

# 분해되지 않는 균형잡힌 문자열의 마지막 문자 Index 반환 
def getIndexForBalanceString(target) :
    
    leftCount = 0
    rightCount = 0 
    
    for index in range(len(target)) :
        if target[index] == '(' :
            leftCount += 1
        else :
            rightCount += 1
        
        if leftCount > 0 and leftCount == rightCount :
            return index

# 올바른 문자열인지 확인 
def isRightString(target) :
    
    stackCount = 0
    
    for char in target :
        if char == '(' :
            stackCount += 1
        else :
            
            if stackCount == 0 :
                return False
            stackCount -= 1
    
    if stackCount != 0 :
        return False
    
    return True

def stage(inputData) :
    
    if inputData == '' :
        return ''
    
    index = getIndexForBalanceString(inputData) 
    
    u = inputData
    v = ''
    
    # 경계값 체크 
    if index != len(inputData) - 1:
        u = inputData[:index + 1]
        v = inputData[index + 1 :]
        
    if isRightString(u) :
        result = stage(v)
        return u + result
    else :
        newString = '('
        result = stage(v)
        newString += result + ')'
        ru = u[1:-1]
        
        newU = ''
        for char in ru :
            if char == '(' :
                newU += ')'
            else :
                newU += '('
        newString += newU
        
        return newString
        

def solution(p):
    
    return stage(p)