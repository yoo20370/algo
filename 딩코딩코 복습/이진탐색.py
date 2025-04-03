
# 이진 탐색은 반드시 정렬되어 있어야 한다. -> 정렬 라이브러리 시간 복잡도 O(NlogN)
def binarySearch(arr, target) -> int :
    pl = 0
    pr = len(arr) -1

    # pl과 pr이 동일한 값인 경우까지 처리해야하기 때문에 <= 사용 
    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < target :
            pl = mid + 1
        elif arr[mid] > target :
            pr = mid - 1
        else :
            return mid
    
    return -1 
            