# 한 번에 한 개의 알파벳만 바꿀 수 있다. 
# words에 있는 단어로만 변환할 수 있다. 

# hit에서 시작해서 words를 순회하면서, 아직 방문하지 않았고, 단어가 하나만 다른 경우
# dfs 수행, 

def check_difference_one_for(word, target) :
    different_count = 0
    
    for index in range(len(word)) :
        if word[index] != target[index] :
            different_count += 1 
    
    return True if different_count == 1 else False

def dfs(curr_word, visited, target, words, count) :
    global min_count 
    
    if curr_word == target :
        min_count = min(min_count, count)
        return 
    
    if count >= len(words) : 
        return 
    
    for index in range(len(words)) :
        if visited[index] and check_difference_one_for(curr_word, words[index]) :
            visited[index] = False
            dfs(words[index], visited, target, words, count + 1)
            visited[index] = True

def solution(begin, target, words):
    
    global min_count
    min_count = 100
    
    visited = [True] * len(words)
    dfs(begin, visited, target, words, 0)
    
    return 0 if min_count == 100 else min_count
    
