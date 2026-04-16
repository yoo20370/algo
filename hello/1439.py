
import sys

def solution() :

    string = sys.stdin.readline().rstrip()

    allZero = allOne = 0

    if string[0] == '0' :
        allOne += 1
    else :
        allZero += 1

    currentChar = string[0]
    for char in string :
        if currentChar != char :
            if char == '0' :
                allOne += 1
            else :
                allZero += 1
            currentChar = char

    minValue = min(allZero, allOne)

    print(minValue)

solution()