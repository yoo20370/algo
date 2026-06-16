## 완주하지 못한 선수 

# 문제가 보면 결국, 있는지도 검사해야 하고, 몇 개가 있는지도 확인해야 함 
# 두 가지가 있음 결국 개수가 그리 많지 않으니 해시 테이블을 직접 만들거나
# 아니면 dict을 사용하고 거기에 개수를 가지고 있게 하는 것임 
# 그리고 참여자가 순회할 때, 감소시켜서 만약 해당 값이 존재하지 않거나 0인 경우는 미참여자로 판단하는 방법 

# 라이브러리를 사용하는 방향으로 가보자 

def solution(participant, completion):
        
    completionDict = {}    
    
    for player in completion :
        
        if completionDict.get(player) is None :
            completionDict[player] = 1
        else :
            completionDict[player] += 1
    
    for player in participant :
        currentValue = completionDict.get(player)
        
        if currentValue is None or currentValue == 0 :
            return player
        else :
            completionDict[player] -= 1
     
    return None