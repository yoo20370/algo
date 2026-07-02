# 처음에 순열과 dfs가 생각났다.
# 순열은 전부 과정이 떠올랐지만, dfs는 어떻게  풀어야할지 확신은 못헀다. 그래서 순열로 풀었다.
# 이번에는 순열이 아닌 dfs로 풀어보려고 한다. 

# 어떻게 풀 것인가 ??
# 일단 dfs()를 호출하도록 한다.
# dfs 내부에서는 dungeons를 순회하게 된다.

def dfs(currentHealth, visited, dungeons) :
    
    maxCount = len(visited)    
    
    for index in range(len(dungeons)) :
        requireHealth, useHealth = dungeons[index]
        
        if requireHealth <= currentHealth and index not in visited :
            visited.add(index)
            maxCount = max(maxCount, dfs(currentHealth - useHealth, visited, dungeons))
            visited.remove(index)
            
    return maxCount

def solution(k, dungeons):
    
    visited = set()
    return dfs(k, visited, dungeons)
    
    