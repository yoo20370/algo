# 균형 괄호 문자열 확인 
def check_balance_string(string) :
    
    count = 0
    for curr in string :
        if curr == "(" :
            count += 1 
        else :  
            count -= 1
    
    # 닫는 괄호, 여는 괄호 수가 같으면 균형잡힌 괄호 
    if count != 0 :
        return False
    
    return True

# 올바른 괄호 문자열 확인 
def check_right_string(string) :
    
    count = 0 
    for curr in string:
        if curr == "(" :
            count += 1
        else : 
            if count == 0 :
                return False
            count -= 1
    
    if count != 0 :
        return False
    
    return True

def change_string(string) :
    temp = ""
    for curr in string:
        if curr == "(" :
            temp += ")"
        else :
            temp += "("
            
    return temp

def solution(p):
    if p == "" :
        return ""
    
    # 전부 올바르면 바로 반환 
    if check_right_string(p) :
        return p
    
    u = ""
    v = ""
    for end_index in range(2, len(p) + 1, 2) :
        u = p[0:end_index]
        if check_balance_string(u) :
            v = p[end_index:]
            break
    
    # u가 올바른 괄호 문자열이라면 -> v에 대해서 재귀 -> 결과를 u에 붙여 함수 반환 
    if check_right_string(u) :
        u += solution(v)
        return u 
    
    # u가 올바른 괄호 문자열이 아니라면 빈 문자열에 대해 수행 
    temp = "(" + solution(v) + ")"
    
    
    # u의 첫 번째 문자와 마지막 문자를 제거 
    if len(u) != 0 :
        u = u[1:-1]
    
    u = change_string(u)
    temp += u
    
    return temp