# 접근 자체를 처음에 완전 탐색으로 접근 
## 그 이유가 모든 경우의 수를 확인을 해야 가장 많은 인원이 참여할 수 있을 것이라 생각 
## 통과는 되지만, 비효율적 
## 굳이 dfs까지 사용할 필요가 없음

# 단순히 앞에서 부터 빌려줄 수 있는 인원이 빌려주는 방향으로 처리하면 됨 
## 이유는 굳이 다른 경우를 고려할 필요가 없음 -> 고려해봤자 왼쪽에서 순서대로 빌려주는 것보다 나은 경우가 없음 

## 여기서 조심해야 하는 건 여벌의 체육복을 가져오는 건 체육복을 도난 당하지도 않고 여벌의 체육복을 가져온 사람 
## 간단하게 생각하면, lost 위치에 대해서 빌려줄 수 있는 인원이 있는지 확인하면 될 듯, 바로 왼쪽 혹은 오른쪽에 존재하는지 확인, 그리고 그 사람이 도난도 당하지 않아고, 여분의 체육복이 있는 경우 count를 올려주면 될 것 같음 

def solution(n, lost, reserve):
    
    # 체육에 참여할 수 인원을 구하자
    # lost에 포함되어 있지만 reverse에 포함되지 않은 인원을 구하고 전체 인원에서 빼주는 방향으로 구하자 
    
    # 순서대로 들어온다거나 안 들어온다는 말이 없음 
    lost.sort()
    
    # 여유분이 있지만, 빌려줄 수 없는 인원을 관리해야 할 것 같음
    canNotLendList = set()
    
    # 여유분이 있었지만 체육복을 도난당한 경우는 빌려줄 수 없으므로 기록 
    for student in reserve :
        if student in lost :
            canNotLendList.add(student)
    
    nonAppearanceCount = 0
    for studentNumber in lost :
        # 여유분이 없는 녀석에 대해서 
        if studentNumber not in reserve :
            
            left = studentNumber - 1 
            # 왼쪽 친구가 빌려줄 수 있다면 
            if left in reserve and left not in canNotLendList :
                canNotLendList.add(left)
                continue
            
            right = studentNumber + 1 
            # 오른쪽 친구가 빌려줄 수 있다면 
            if right in reserve and right not in canNotLendList :
                canNotLendList.add(right)
                continue
                    
            # 도난 당했고, 왼쪽 오른쪽 둘 다 빌려줄 수 없는 상황이라면
            nonAppearanceCount += 1
            
    return n - nonAppearanceCount