import sys

def backTracking(length, result, N, M) :

    if length == M :
        for number in result :
            print(number + 1, end=" ")
        print()
        return 

    for index in range(N) :
        if index not in result :
            if not result or (result and result[-1] < index):
                result.append(index)
                backTracking(length + 1, result, N, M)
                result.pop()

def solution() :

    N, M = map(int, sys.stdin.readline().split())

    backTracking(0, [], N, M)


solution()