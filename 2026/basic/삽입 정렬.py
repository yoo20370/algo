input = [4, 6, 2, 9, 1]

# 삽입 정렬이랑 해당 원소가 삽입될 위치를 찾아가는 정렬 알고리즘

## 원소가 삽입 될 위치를 찾아야 현재 위치 -1 ~ 0까지 이동하며, 삽입할 위치를 찾는다. (각 단계의 최악의 경우)
## 만약 이전 원소가 값이 더 크다면, 이전 원소의 값을 현재 위치로 이동시킨다. 
## 그리고 삽입할 위치가 정해지면 

## 바깥 반복문은 원소를 가리켜야 함 즉, 1 ~ n까지 가리켜야 함 
## 안쪽 반복문은 앞으로 이동하면서, 선택된 원소가 삽입될 위치를 찾도록 해야 함 


def insertion_sort(array):

    length = len(array)
    
    for i in range(1, length) : 
        value = array[i]
        j = i 
        while j - 1 >= 0 and array[j-1] > value : 
            array[j] = array[j-1]
            j -= 1
        array[j] = value

    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))