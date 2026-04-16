input = [4, 6, 2, 9, 1]

## 선택 정렬이란 특정 위치에 삽입할 원소를 선택하는 정렬 
## 매번 순회하면서, 삽입할 원소를 찾아야 함 
# 내부 반복문은 length - 1 번 실행하면 될 것 같음 -> 마지막 원소는 알아서 자동 확정될 것으로 추측 
# 외부 반복문의 인덱스는 삽입할 index로 생각하면 될 듯 
# 내부 반복문은 N - 1, N - 2, N - 3 번 순회하면서 최소값 혹은 최대값을 찾으면 될 것 같음 

def selection_sort(array):

    # 이 부분을 채워보세요!

    length = len(array)

    for i in range(length - 1) :

        minNumberIndex = i
        for j in range(i + 1, length, 1) :
            if array[j] < array[minNumberIndex] :
                minNumberIndex = j
        
        array[i], array[minNumberIndex] = array[minNumberIndex], array[i]
            

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))