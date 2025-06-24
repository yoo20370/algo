# 고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미 
import sys 

def binary_search(array, target) :

    pl = 0
    pr = len(array) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if array[mid] < target :
            pl = mid + 1
        elif array[mid] > target :
            pr = mid - 1
        else :
            return mid

    return - 1

def solution() :

    length = int(sys.stdin.readline().rstrip())

    data = list(map(int, sys.stdin.readline().split()))

    pl = 0
    pr = len(data) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if data[mid] == mid :
            return mid
        elif data[mid] < mid :
            pl = mid + 1
        else :
            pr = mid - 1

    return - 1

print(solution())