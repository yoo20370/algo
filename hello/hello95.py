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
    
