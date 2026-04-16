# 어떻게 접근해야 하지 ?? 
# 6 9 5 7 4 - > N ** 2 
# 비교하는 횟수를 줄여야 함 -> 여기서 패턴을 찾아야 함 
# 어떻게 줄이지 ?? 
# 가장 먼저 닿는 거네 ?? 
# 그럼 만약에 특정 탑의 레이저가 닿았다면 ?? 나에게 닿지 않은 녀석들은 닿는거 아닌가 ?? 
# 즉, 내가 닿았다는 건, 내 이전에 닿지 않았던 탑이 닿을 가능성이 있다는 말 아닌가 ?? 

# 정리하자면 
# 현재 탑이 바로 앞 탑에 레이저를 쐈을 때 맞지 않음 그렇다는 건 앞으로 이동해서 확인해야 한다는 소리
# 근데 어짜피 바로 앞 탑이 이걸 반복해야 함 그러니 앞의 탑이 쏴서 맞췄을 때, 한 번더 꺼내서 비교하면 됨 -> 그렇지 않으면 굳이 비교할 필요 없음
# 만약 맞았다면 나도 비교해볼 가치가 있음 (나도 맞출 수 있기 때문)

import sys

def solution() :
    count = int(sys.stdin.readline().rstrip())

    towers = list(map(int, sys.stdin.readline().split()))

    result = [0] * count

    stack = []

    while towers :
        currentheight = towers.pop()
        currentIndex = len(towers)

        if towers and currentheight <= towers[-1] :
            # 맞춘거임 맞지 ?? 그럼 결과에 기록해야 함 
            result[currentIndex] = len(towers)

            while stack and stack[-1][0] <= towers[-1] :
                currentheight, currentIndex = stack.pop()
                result[currentIndex] = len(towers)
        else : 
            stack.append([currentheight, currentIndex])
    
    for i in result :
        print(i, end = " ")

solution()
