# 백트래킹 같음 

order = 0 

def dfs(currentWord, targetWord, currentOrder) :
    
    global order
    
    # 길이 제한 
    if len(currentWord) > 5 :
        return currentOrder - 1
    
    # 아예 끝나야 하는데 그게 아님 더 진행되는거임 
    if currentWord == targetWord :
        order = currentOrder
        return currentOrder
    
    for char in ['A', 'E', 'I', 'O', 'U'] :
        temp = currentWord + char
        currentOrder = dfs(temp, targetWord, currentOrder + 1)
    
    return currentOrder
    
def solution(word):
    currentWord = ''
    currentOrder = 0
    
    dfs(currentWord, word, currentOrder)
    
    return order