# 일정 피로도 사용해서 던전 탐험 
# 각 던전마다 최소 필요 피로도, 소모 피로도가 존재
# 최소 필요 피로도는 던전을 탐험하기 위해 가지고 있어야 함 
# 소모 피로도는 탐험 후, 소모되는 피로도 

# 하루에 한 번씩 탐험할 수 있는 던전이 여러 개 있음
# 한 유저가 최대한 많은 던전을 탐험하려고 함 
# 한 유저의 현재 피로도 K가 주어짐
# 이 유저가 던전을 최대한 많이 돌도록 만들어라 

## 그럼, 피로도가 가장 적게 줄어드는 던전부터 돌아야 함
## 또한 최소 피로도는 큰 것부터 나열되어야 함 
## 근데 여기서 문제점은 뭐냐면, 소모 피로도는 10인데 최소 피로도가 100인 경우가 있을 수 있음 
## 그러면 그냥 모든 경우의 수를 다 해보고 탐험 가장 많이 한 것을 선택하는게 좋을지도 
# import itertools 

# def solution(k, dungeons):
    
#     max_count = 0
#     for x in itertools.permutations(dungeons, len(dungeons)) :
#         curr_k = k 
#         count = 0
#         for min_fitigue, fitigue in x:
#             if min_fitigue <= curr_k :
#                 curr_k -= fitigue
#                 count += 1
        
#         max_count = max(max_count, count)

#     return max_count

# dfs로 풀어본다 -> 사실, dfs가 먼저 떠올랐지만 시간복잡도 계산해보니 가능할 것 같아서 itertools로 풀었음 

# 어떻게 풀까
# 매번 독립적인 방문set, health_point를 가져야하므로 재귀 dfs를 사용한다.
# 현재 index를 방문처리하고, 던전 목록을 순회하면서 아직 방문하지 않은 던전을 확인한다.
# 이때, 중요한 건, 피로도로 인해 방문 할 수 있던, 못하던 방문 처리를 해줘야 함
# visited의 크기가 dungeons 크기와 동일하다면, 지금까지 카운트한 값을 max_count와 비교하여
# 가장 큰 count를 결정한다. 

# max_count = 0
# def dfs(curr_index, curr_visited, curr_remain_health_point, dungeons, curr_count) :
#     curr_visited.add(curr_index)
    
#     if len(curr_visited) == len(dungeons) :
#         global max_count 
#         max_count = max(max_count, curr_count)
#         return
    
#     for index in range(len(dungeons)) :
#         remain_health_point = curr_remain_health_point
#         count = curr_count 
        
#         if index not in curr_visited :
#             min_fitigue, fitigue = dungeons[index]
            
#             if min_fitigue <= remain_health_point :
#                 remain_health_point -= fitigue
#                 count += 1
            
#             dfs(index, set(curr_visited), remain_health_point, dungeons, count)

# def solution(k, dungeons):
    
#     for start_index in range(len(dungeons)) :
#         health_point = k
#         count = 0 
#         visited = set()
        
#         min_fitigue, fitigue = dungeons[start_index]
        
#         if min_fitigue <= health_point :
#             health_point -= fitigue
#             count += 1

#         dfs(start_index, visited, health_point, dungeons, count)

#     return max_count

## 백트래킹 적용
def dfs(k, dungeons, visited, count) :
    global max_count 
    max_count = max(max_count, count)
    
    for i in range(len(dungeons)) :
        if not visited[i] :
            min_fitigue, fitigue = dungeons[i]
            if k >= min_fitigue :
                visited[i] = True
                dfs(k-fitigue, dungeons, visited, count + 1)
                visited[i] = False

def solution(k, dungeons):
    global max_count 
    max_count = 0
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return max_count