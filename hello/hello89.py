# 결국 그거 아님 ?? 가장 앞에 있는 hIndex 후보에 대해서 위치를 확인 
# 그리고 hIndex 후보를 포함해서 큰 값이 몇 개인지 확인 -> 만약 hIndex 개수보다 크다면 만족
# 그리고 나머지 hIndex 제외한 나머지의 개수가 H 이하인지 확인 
def solution(citations):
    
    hIndex = 0 
    hIndexLocation = 0
    sortedCitations = sorted(citations)
    
    length = len(sortedCitations)
    
    while hIndexLocation < length :
        candiateHIndex = hIndex + 1
    
        while hIndexLocation < length and sortedCitations[hIndexLocation] < candiateHIndex :
            hIndexLocation += 1
        
        # 접근 인덱스가 초과했는지 확인 
        if hIndexLocation >= length :
            break
        
        # 인용된 논문 개수 
        BigCount = length - hIndexLocation
        # 나머지 논문 개수 
        RemainCount = length - BigCount
        
        # 조건에 맞는지 
        if candiateHIndex <= BigCount and RemainCount <= candiateHIndex :
            hIndex = candiateHIndex
            continue
        
        # 조건에 맞지 않는다면 
        break
    
    return hIndex