import sys 

## 이진 탐색은 중간 값을 구하고 그 값이 target인지 확인함 

finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
finding_target = 14

def binarySearch(array, target) :
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
        
    return -1

result = binarySearch(finding_numbers, finding_target)
print(result)
        
