import sys

def solution() :
    
    firstNumber, lastNumber = map(int, sys.stdin.readline().split())

    primeList = [True] * (lastNumber + 1)
    primeList[0] = primeList[1] = False

    # 곱하는 수는 대칭 
    # 전부할 필요 없음 
    for number in range(2, int(lastNumber ** (1/2)) + 1) :
        
        if primeList[number] : 
            current = number
            while number * current <= lastNumber :
                primeList[number * current] = False
                current += 1
    

    for number in range(firstNumber, lastNumber + 1) :
        if primeList[number] :
            print(number)


solution()

