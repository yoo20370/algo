# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여할 수 있도록 규정
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금 

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여
# 모든 모험가를 특정 그룹에 넣을 필요는 없음 
# 작은 수부터 시작해서, 공포도와 현재 인원을 만족하는 그룹을 만든다. -> 공포도가 낮을 수록 적은 인원이 필요하기 때문, 모든 모험가를 특정 그룹에 넣을 필요가 없기 떄문 


# 어떻게 풀까 ?? 
# 순회하면서 currentPersonnel이 현재 모험가의 공포도보다 작다면
# currentPersonnel += 1하고 다음으로 넘어간다. 

# 만약 currentPersonnel이 현재 모험가의 공포도보다 크거나 같다면 groupCount를 증가시키고 currentPersonnel을 초기화한다. 

import sys

def solution(member, k) :
    
    groupCount = 0

    member.sort()

    currentPersonnel = 0
    for currentFearLevel in member :

        # 본인 포함한 인원 
        nextPersonnel = currentPersonnel + 1

        if currentFearLevel <= nextPersonnel :
            groupCount += 1
            currentPersonnel = 0
        else :
            currentPersonnel = nextPersonnel
    
    return groupCount


k = sys.stdin.readline().rstrip()
member = list(map(int, sys.stdin.readline().split()))

result = solution(member, k)
print(result)