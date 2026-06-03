import sys

count = 6

def solution() :

    maxNumber = 0
    maxIndex = 0

    currentIndex = 0

    for _ in range(count) :
        input = int(sys.stdin.readline().rstrip())

        if input > maxNumber :
            maxNumber = input
            maxIndex = currentIndex 
        
        currentIndex += 1

    print(maxNumber)
    print(maxIndex + 1)

solution()