# 현재 문자에서 갈 수 있는 다른 문자를 찾아야 함 
# words 순회하면서 현재 문자에서 이동할 수 있는 문자로 이동한다. 문자 이동 각각은 독립적으로 움직인다. 전역탐색 ? 
# 이때 이동할 문자를 큐에 넣을때 현재 turn + 큐 튜플 형태로 저장한다. 

from collections import deque

def isOneCharDifferent(wordA, wordB) :
     
    count = 0
    for index in range(len(wordA)) :
        if wordA[index] != wordB[index] :
            count += 1
    
    if count == 1 :
        return True
    else : 
        return False


def solution(begin, target, words):
    
    visited = set()
    
    queue = deque()
    queue.append((begin, 0))
    visited.add(begin)
    
    while queue :
        currentWord, currentCount = queue.popleft()
        
        if currentWord == target :
            return currentCount
        
        for word in words :
            if isOneCharDifferent(currentWord, word) and word not in visited :
                queue.append((word, currentCount + 1))
                visited.add(word)
                
    return 0