# 올바른 괄호

# 열렸으면 닫히는게 있어야 함 
# '(' 이면 스택에 삽입 
# ')' 이면 스택에서 '(' 제거 
# 만약 제거하려고 할 때 '(' 없으면 false 반환 
# 순회를 마쳤는데 Stack이 비어있지 않으면 false 반환 

## 근데 꼭 스택을 사용해야 해 ?? 그냥 숫자 가지고 해결해도 될 것 같은데 ?? 
## 스택을 사용할 필요가 없음 
## 개수가 맞는지만 판별하면 되기 때문 

def solution(s):
    
    stackCount = 0 
    
    for char in s :
        if char == '(' :
            stackCount += 1
        
        else :
            if stackCount <= 0 :
                return False
            stackCount -= 1

    if stackCount != 0 :
        return False
            
    return True