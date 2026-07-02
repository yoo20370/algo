# 일정 피로도를 사용해서 던전을 탐험
# 탐험을 위해 필요한 최소 필요 피로도와 소모 피로도가 있음 
# 최소 필요 피로도 - 던전을 탐험을 위해 가지고 있어야 하는 피로도
# 소모 피로도는 - 던전을 탐험한 후 소모되는 피로도 

# 하루에 한 번씩 탐험할 수 있는 던전이 여러 개
# 한 유저가 오늘 이 던전들을 최대한 많이 탐험 
# 유저의 현재 피로도 K와 각 던전별 최소 필요 피로도, 소모 피로도가 담긴 2차원 배열 dungeons가 매개 변수로 주어질 때,
# 유저가 탐험할 수 있는 최대 던전 수를 return 하라 

## 모든 경우의 수를 비교해서 가장 많이 방문한 경우를 확인해야 할 것 같음 
## 어떻게 방문하도록 해야하나 ?? 
## 또 순열인가 ?? 

## 순열을 통해서 접근할 순서를 결정한다. 
## 이 중 순서대로 가능한 경우까지만 도전, 만약 더 이상 접근 불가능한 경우 거기가 최대값임 

# 시간 복잡도는 N! * N 라고 생각
# 순열을 통해서 순서 결정 
# 최대 N번 방문할 수 있으므로 O(N * N!)이라고 생각 
# 던전의 개수가 최대 8이므로 가능한 시간복잡도 

from itertools import permutations

def getExploreCount(dungeons, k) :
    
    currentHealth = k 
    exploreCount = 0
    for dungeon in dungeons :
        requiredHealth, useHealth = dungeon 
        
        if requiredHealth <= currentHealth :
            exploreCount += 1
            currentHealth -= useHealth
        else :
            return exploreCount
    
    return exploreCount

def solution(k, dungeons):
    
    maxCount = 0
    for dungeonList in permutations(dungeons, len(dungeons)) :
        result = getExploreCount(dungeonList, k)
        maxCount = max(maxCount, result)
    
    return maxCount