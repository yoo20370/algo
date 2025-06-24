# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음 
# 이때, 이 수열에서 X가 등장하는 횟수를 계산하여라 

# O(lgN)으로 알고리즘을 설계하지 않으면 시간 초과 발생 
 
# 0 1 2 3 4 5 6 
# 1 1 2 2 2 2 3
# 5 - 2 + 1 -> 해당 언소 개수 
import sys 

def binary_search_left(array, target) :
    pl = 0 
    pr = len(array) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if array[mid] < target :
            pl = mid + 1
        elif array[mid] > target :
            pr = mid - 1
        else :
            if mid > 0 and array[mid-1] == target :
                pr = mid - 1
            else :
                return mid     
    return -1

def binary_search_right(array, target) :
    pl = 0 
    pr = len(array) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if array[mid] < target :
            pl = mid + 1
        elif array[mid] > target :
            pr = mid - 1
        else :
            if mid != len(array) - 1 and array[mid+1] == target :
                pl = mid + 1
            else :
                return mid     
    return -1

def solution() :
    length, target = map(int, sys.stdin.readline().split())

    array = list(map(int, sys.stdin.readline().split()))

    left_index = binary_search_left(array, target)
    right_index = binary_search_right(array, target)

    
    if left_index == -1 or right_index == -1 :
        return -1 
    else :
        return right_index - left_index + 1

print(solution())