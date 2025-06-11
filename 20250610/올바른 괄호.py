def is_correct_parenthesis(string):
    # 여는 괄호가 들어오면 스택에 push
    # 닫는 괄호가 들어오면 스택에서 pop - 비어있을 때, pop 하면 False 반환 
    # 모든 문자열 순회 후, stack이 남아 있으면 False 반환
    # 모든 과정 수행 후 문제 없다면 True 반환 
 
    stack = []

    for char in string :
        if char == '(' :
            stack.append(True)

        else : 
            if not stack : 
                return False 
            stack.pop()
    
    if stack :
        return False
        
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))