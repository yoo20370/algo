# 떡볶이의 떡 길이가 일정하지 않음 
# 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다. 
# 절단기 높이 H를 지정하면 줄지어진 떡을 한 번에 절단 
# 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것 
# 낮은 떡은 잘리지 않음 

# 손님이 요구하는 총 길이가 M일 때, 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이 최대값 
# 결국 높이를 계속 높여가며 확인해라 그 중 길이 합이 M을 넘는 경우는 무엇인가 ?

# 구해야 하는 건 절단기 최대 높이 
# 잘려진 떡을 주는거임 


import sys

def cutAndSum(riceCakeList, cutterHeight) :

    totalRiceCakeLength = 0 

    for currentRiceCakeLength in riceCakeList :
        # 잘리지 않음 
        if currentRiceCakeLength <= cutterHeight : 
            continue
        
        cuttingLength = currentRiceCakeLength - cutterHeight
        totalRiceCakeLength += cuttingLength
        
    return totalRiceCakeLength

def solution() :

    riceCakeCount, requestRiceCakeLength = map(int, sys.stdin.readline().split())
    riceCakeList = list(map(int, sys.stdin.readline().split()))

    # 절단기 높이를 구함 -> 절단기 높이 기준으로 떡들 잘라서 합을 구하면 됨 그래서 요구하는 높이를 넘는지 확인하면 됨 
    # 높이를 계속해서 구해서 확인하는 과정이 필요함 -> 그걸 다하면 불가능함 그 이유는 잘라서 100만개를 더해야함 
    # 줄여야 하는 건 뭐지 ?? -> 높이 탐색하는 과정을 줄여야 함 
    # 그 이유는 떡을 자른 후, 그 값을 합하는 건 무조건 해야함 그렇기에 줄일 수 없음

    # 절단기 높이의 범위를 절반씩 줄여가며, 떡의 길이의 합이 넘는지 안 넘는지를 기준으로 처리하면 될 것 같음 

    minCutterHeight = 0
    maxCutterHeight = max(riceCakeList)

    bestCutterHeight = maxCutterHeight
    
    while minCutterHeight <= maxCutterHeight :
        midCutterHeight = (minCutterHeight + maxCutterHeight) // 2

        totalRiceCakeLength = cutAndSum(riceCakeList, midCutterHeight)
        if totalRiceCakeLength < requestRiceCakeLength :
            # 잘라진 길이가 요구보다 작다면, 높이를 줄여야함 -> 그래야 길이가 커짐 
            maxCutterHeight = midCutterHeight - 1
        
        elif totalRiceCakeLength >= requestRiceCakeLength :
            # 잘라진 길이가 요구보다 크다면, 높이를 높여야지 -> 그래야 길이가 작아짐

            # 왜 기록함 -> 현재 가장 절단기 높이가 길어서 기록해야 함 
            bestCutterHeight = midCutterHeight
            minCutterHeight = midCutterHeight + 1

    print(bestCutterHeight)
            
solution()