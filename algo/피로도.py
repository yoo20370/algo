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
import itertools 

def solution(k, dungeons):
    
    max_count = 0
    for x in itertools.permutations(dungeons, len(dungeons)) :
        curr_k = k 
        count = 0
        for min_fitigue, fitigue in x:
            if min_fitigue <= curr_k :
                curr_k -= fitigue
                count += 1
        
        max_count = max(max_count, count)

    return max_count