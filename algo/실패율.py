# 실패율을 구해야 한다.

## 스테이지에 도달한 플레이어 수 -> 스테이지 >= 현재 스테이지 
## 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 -> 현재 스테이지인 사람들 

# N이 주어졌으니까 
# 1 ~ N 스테이지까지 순차적으로 진행하는게 좋을 것 같다.
# a 스테이지를 찾기 위해 stage를 순회한다. 

# 어디서 런타임이 발생하는가 ?? 

MX = 505

def solution(N, stages):
    
    answer = []
    
    table = [0] * MX
    stages.sort()
    
    for stage in stages :
        table[stage] += 1 
    
    curr_index = 0
    for stage in range(1, N + 1) :
        # stage값일 수도 그보다 클 수도 있음 
        while curr_index < len(stages) and stages[curr_index] < stage : 
            curr_index += 1 
        
        # 스테이지에 도달한 플레이어의 수
        length = len(stages[curr_index:])
        if table[stage] == 0 :
            result = 0
        else :
            result = table[stage] / length  
        answer.append((result, stage))
    
    answer.sort(reverse=True, key=lambda x : (x[0], -x[1]))
    answer = [j for i , j in answer]
    
    return answer