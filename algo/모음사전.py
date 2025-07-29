import sys
sys.setrecursionlimit(int(1e9))

# 어떻게 풀어야 하는가 ?? 
# 어떻게 증가시켜야 하지 ?? dfs 백트래킹 어때 ?? 
# 처음에 A로 시작하고 그 dfs 함수는 A부터 U까지 하는 책임을 갖는다. 
# 또 dfs()가 재귀를 타면 그 재귀는 A부터 U까지 출력하는 책임을 갖는거지 
# dfs를 타는 것은 전체 길이가 5가 될 때까지 하는거지 
# 일단 떠오르는 건 이거임 풀어보자 
# 빈 글자로 시작해서 각 글자수에서 A E I O U를 반복할 예정 

def dfs(curr_string) :
    global count 
    global answer
    global target

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
    global count 
    global answer
    global target 
    target = word
    count = 0
    
    dfs("")
    
    return answer