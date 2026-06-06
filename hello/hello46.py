# mergeSort
# 병합 정렬
# 배열의 크기가 1이 될 때까지 모두 나눈다 -> lgN 
# 각 배열을 순회하며 값을 비교하고 하나의 배열로 만든다. (N번 비교)
# 항상 NlgN 시간 복잡도를 필요로 한다.
# 안정정렬, 제자리 정렬 X

data = [13, 4, 19, 1, 8, 16, 5, 11, 20, 3, 14, 7, 18, 10, 2, 15, 6, 17, 9, 12]

def mergeSort(data) :
    

    length = len(data)

    if length <= 1 :
        return data 
    

    pl = 0 
    pr = length - 1

    mid = (pl + pr) // 2

    # 왼쪽, 오른쪽으로 분할 -> 언제까지 ? 크기가 1이 될 때까지 
    left = mergeSort(data[:mid + 1])
    right = mergeSort(data[mid + 1:])

    result = []

    leftIndex = rightIndex = 0 

    # 두 배열을 비교해서 작은 값부터 차례대로 result에 추가 
    while leftIndex < len(left) and rightIndex < len(right) :
        if left[leftIndex] < right[rightIndex] :
            result.append(left[leftIndex])
            leftIndex += 1
        else :
            result.append(right[rightIndex])
            rightIndex += 1

    # 남은 값 모두 넣기 
    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])

    return result
 
def solution() :

    result = mergeSort(data) 

    print(result)


solution()
