# (가 들어오면 스택에 0 삽입 )가 들어오면 스택에서 제거 
# )가 등장했는데 스택이 비어있다면 False 반환
# 모두 진행 후 리스트의 길이가 0이 아니라면 False 반환 

def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []

    for ch in string :

        if ch == "(" :
            stack.append(0)

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