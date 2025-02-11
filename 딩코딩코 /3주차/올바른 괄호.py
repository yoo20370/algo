def is_correct_parenthesis(string):
    
    # '('가 입력으로 들어오면 스택에 넣는다. 
    # ')'가 입력으로 들어오면 스택에서 '('를 하나 뺀다. 
    # ')'가 입력으로 들어왔을 때, 스택이 비어있다면 False를 반환
    # 모든 입력이 끝났음에도 '(' 이 하나 이상 남은 경우 False를 반환

    stack = []
    for char in string :
        if char == '(' :
            stack.append('(')
            continue

        if not stack :
            return "False"
        stack.pop()
    
    if stack :
        return False
       
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))