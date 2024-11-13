# # 병합 정렬 
# # 재귀 함수 

# N = int(input())

# data = list()
# for i in range(N) :
#     data.append(int(input()))

# def mergeSort(arr) :
#     length = len(arr) 

#     if length == 1 :
#         return arr 

#     pl = 0
#     pr = length - 1
#     mid = length // 2

#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])

#     result = list()
#     left_idx = 0
#     right_idx = 0

#     while left_idx < len(left) and right_idx < len(right) :
#         if left[left_idx] < right[right_idx] :
#             result.append(left[left_idx])
#             left_idx += 1
#         else :
#             result.append(right[right_idx])
#             right_idx += 1
    
#     result.extend(left[left_idx:])
#     result.extend(right[right_idx:])

#     return result

# data = mergeSort(data)

# for i in data :
#     print(i)

# 퀵 정렬 

N = int(input())

data = list()
for i in range(N) :
    data.append(int(input()))

def quickSort(arr, left, right) : 

    
    pl = left
    pr = right
    # (left + right) // 2 처럼 인덱스를 계산하면 arr[p] 값이 중간에 변경될 수 있음 
    # arr[p]의 경우 pl이 p를 선택하고 pr이 다른 원소를 선택하다가 변경될 수 있음 (항상 그런 것은 아님)
    p = arr[(left + right) // 2]

    # 등호를 붙이는 이유는, 같은 위치에서의 교환을 통해 pl += 1, pr -=1를 수행하지 않아, 분할이 제대로 되지 않음 
    while pl <= pr :
        while arr[pl] < arr[p] :
            pl += 1
        while arr[pr] > arr[p] :
            pr -= 1
        
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    # 배열 원소가 하나가 아닐 떄를 고려한 조건문
    if left < pr :
        quickSort(arr, left, pr )
        
    # 배열 원소가 하나가 아닐 떄를 고려한 조건문
    if right > pl :
        quickSort(arr, pl , right)

quickSort(data,0, len(data) - 1)

for i in data :
    print(i)