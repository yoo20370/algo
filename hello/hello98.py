# 한 번에 한 개의 알파벳만 바꿀 수 있음
# words에 있는 단어로만 변환할 수 있음 

# begin을 시작으로 변환할 수 있는 가능한 경우를 모두 탐색한다.
# 그 중 최소값 구하면 될 듯 
# 깊이 우선 탐색 문제인 듯 

INF = int(1e9)

def getDifferentCount(currentWord, targetWord) :
    
    differentCount = 0
    for index in range(len(currentWord)) :
        if currentWord[index] != targetWord[index] :
            differentCount += 1
        
    return differentCount
    
def solution(begin, target, words):
    
    minChangeCount = INF
    
    # (현재단어, 변경 카운트)
    stack = [(begin, 0)]
    
    visited = set()        
    
    # 스택에 카운트랑 같이 튜플 형태로 넣어야 함 -> 특정 단어가 어떤 형태로 이동할지 경우의 수를 모두 따져야 하니까 
    # 근데 visited를 하는 이유는 나중에 거쳐간 경우는 굳이 고려할 필요가 없음 그래서 방문처리해서 중복을 제거해주는 거임 
    
    while stack :
        currentWord, currentCount = queue.pop()
        
        if currentWord in visited :
            continue
        
        visited.add(currentWord)
        # 도달 가능한 여러 가지 수 중 하나일 뿐이므로 함수 자체를 종료시키면 안 됨 
        # 해당 단어는 끝났으며 현재 경우에 대해서 추가적으로 스택에 넣을 필요 없으므로 continue
        if currentWord == target :
            minChangeCount = min(minChangeCount, currentCount)
            continue
        
        for word in words :
            differtCount = getDifferentCount(currentWord, word)
            
            if differtCount == 1 and word not in visited :
                stack.append((word, currentCount + 1))
    
    if minChangeCount == INF :
        return 0
    
    return minChangeCount