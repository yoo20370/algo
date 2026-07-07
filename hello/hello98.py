# 한 번에 한 개의 알파벳만 바꿀 수 있음
# words에 있는 단어로만 변환할 수 있음 

# begin을 시작으로 변환할 수 있는 가능한 경우를 모두 탐색한다.
# 그 중 최소값 구하면 될 듯 
# 깊이 우선 탐색 문제인 듯 

# 깊이 우선 탐색을 수행할 경우, 최소경로가 스택 앞 부분에 문제를 틀릴 수 있음
# 고로 깊이 우선 탐색 보다는 너비 우선 탐색을 통해서 처리하는게 맞는 듯
# 그 이유는 큐 같은 경우는 FIFO 이므로 앞에서 부터 차근차근 처리하므로 괜찮음 

from collections import deque

INF = int(1e9)

def getDifferentCount(currentWord, targetWord) :
    
    differentCount = 0
    for index in range(len(currentWord)) :
        if currentWord[index] != targetWord[index] :
            differentCount += 1
        
    return differentCount
    
def solution(begin, target, words):
    
    minChangeCount = INF
    
    queue = deque([(begin, 0)])


    visited = set()        
    
    while queue :
        currentWord, currentCount = queue.popleft()
        
        if currentWord in visited :
            continue
        
        visited.add(currentWord)
    
        if currentWord == target :
            minChangeCount = min(minChangeCount, currentCount)
            continue
        
        for word in words :
            differtCount = getDifferentCount(currentWord, word)
            
            if differtCount == 1 and word not in visited :
                queue.append((word, currentCount + 1))
    
    if minChangeCount == INF :
        return 0
    
    return minChangeCount