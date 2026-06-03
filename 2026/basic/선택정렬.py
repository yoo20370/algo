input = [4, 6, 2, 9, 1]

## 선택 정렬이라는 건 비교 원소 중에서 특정 조건을 만족하는 원소를 선택해서 정렬하는 알고리즘 
## 바깥 반복문은 선택된 원소를 저장할 위치를 기록하는 변수값을 갖는다. 0 ~ n-1 (마지막 원소는 마지막 전 원소가 확정되면 자동 확정되기 때문)
## 내부 반복문은 비교해야 하는 원소에 대해서 항상 순회하여 min 값을 찾는다. 

## 선택 정렬은 제자리 정렬이다. (추가적인 메모리 공간이 필요하지 않음)
## 선택 정렬은 불안정 정렬이다. (두 포인트에 대해서 교환할 때 순서가 엉킬 수 있음)

def selection_sort(array):

    length = len(array)

    for i in range(0, length - 1) :
        minIndex = i
        for j in range(i + 1, length) :
            if array[minIndex] > array[j] :
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))