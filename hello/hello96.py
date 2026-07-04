import sys
sys.setrecursionlimit(int(1e9))

def dfs(curr_string) :
    global count, answer, target

    if answer != -1 :
        return

    if curr_string == target :
        answer = count
        return
        
    if len(curr_string) > 4 :
        return 
    
    for char in ["A", "E", "I", "O", "U"] :
        # 길이 증가 시킴 
        count += 1
        dfs(curr_string + char)
        

def solution(word):
    global count, answer, target 
    answer = -1
    target = word
    count = 0
    
    dfs("")
    
    return answer