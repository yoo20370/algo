# 탑 

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
            
            result[currentIndex] = len(towers)

            while stack and stack[-1][0] <= towers[-1] :
                currentheight, currentIndex = stack.pop()
                result[currentIndex] = len(towers)
        else : 
            stack.append([currentheight, currentIndex])
    
    for i in result :
        print(i, end = " ")

solution()
