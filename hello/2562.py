# 변수 두 개 사용 - 최대값이 무엇인지, 최대값의 위치는 몇인지 
# 들어오는 값을 순회하면서 확인할 것 

import sys

def solution() :
    maxValue = 0 
    maxLocation = 0

    for currentLocation in range(1, 10) : # O(1) 
        currentValue = int(sys.stdin.readline().rstrip())

        if maxValue < currentValue :
            maxValue = currentValue
            maxLocation = currentLocation

    print(maxValue)
    print(maxLocation)

solution()




