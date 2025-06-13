# 버블 정렬
# 버블 정렬이란 인접한 원소를 비교하며 정렬을 수행하는 정렬 알고리즘, 제자리 정렬이며, 안정 정렬이다. O(n**2) 시간 복잡도를 갖는다.

array1 = [5,8,4,7,7]
array2 = [3,-1,17,9]
array3 = [100,56,-3,32,44]

def bubble_sort(array) :

    for i in range(1, len(array)) :  
        for j in range(len(array) - i) : 
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

print(bubble_sort([5,8,4,7,7]))
print(bubble_sort([3,-1,17,9]))
print(bubble_sort([100,56,-3,32,44]))
print()
print()


# 선택 정렬 
# 선택 정렬이란, 특정 위치에 삽입할 원소를 선택하고 선택한 원소를 특정 위치에 삽입하는 정렬 알고리즘, 제자리 정렬, 불안정 정렬

def select_sort(array) :

    for i in range(len(array)-1) : # 첫 번째 부터, 마지막 전 원소까지만 확정하면, 마지막은 알아서 확정됨
        min_index = i
        for j in range(i + 1, len(array)) : # 확정된 녀석은 다시 검사할 필요가 없기 때문에 i부터 시작 
            if array[min_index] > array[j] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


    return array

print(select_sort(array1))
print(select_sort(array2))
print(select_sort(array3))
print()
print()

# 삽입 정렬 
# 삽입 정렬이란, 원소가 삽입될 위치를 앞으로 이동하며 찾아 삽입하는 정렬 알고리즘이다. 앞의 원소들이 정렬되어 있다면 바로 다음 단계로 넘어가고, 모두 정렬되어 있다면 O(n) 시간복잡도에
# 정렬이 가능한 알고리즘이다. 

def insert_sort(array) :

    # i는 원소의 위치 
    for i in range(1, len(array)) :
        target = array[i]
        insert_index = i

        # 해당 원소를 앞의 원소들과 비교하면서, 삽입할 위치를 찾는다. 
        while insert_index - 1 >= 0 and array[insert_index] > target :
            array[insert_index] = array[insert_index - 1]
            insert_index -= 1
        array[insert_index] = target

    return array

print(insert_sort(array1))
print(insert_sort(array2))
print(insert_sort(array3))
print()
print()

# 퀵 정렬
# 퀵 정렬은 분할 정복 알고리즘을 활용한 정렬 알고리즘, 투 포인터를 이용해서 원소 교체를 수행하며, 재귀를 통해 정렬 범위를 쪼개어 정렬을 수행한다. 
# 퀵 정렬은 절반씩 범위를 줄여가며 수행하면 logN의 레벨이 생기고, 각 레벨에 대해서 N 번의 비교를 수행하기 때문에 O(nlgN) 시간 복잡도가 필요하다.

def quick_sort(array, left, right) :

    pl = left
    pr = right
    pivot = array[(pl + pr) // 2] # 피벗을 값으로 둬야 함 -> pivot 값이 중간에 변할 수 있음 

    while pl <= pr : # pl <= pr 인 이유는 서로 동일한 값일 때, 교차되도록 이동해야 하기 때문 
        while array[pl] < pivot : # 피봇 보다 작은 큰 찾을 때까지 이동 
            pl += 1
        
        while array[pr] > pivot : # 피봇 보다 작은 값을 찾을 때까지 이동 
            pr -= 1

        if pl <= pr :
            array[pl], array[pr] = array[pr], array[pl] # 피봇을 중심으로 잘못된 위치에 있는 원소를 교환함 
            pl += 1
            pr -= 1
    
    if pl < right :
        quick_sort(array, pl, right)
    
    if pr > left :
        quick_sort(array, left, pr)

    
    return array

print(quick_sort(array1, 0, len(array1) - 1))
print(quick_sort(array2, 0, len(array2) - 1))
print(quick_sort(array3, 0, len(array3) - 1))
print()
print()

# 병합정렬 
# 병합 정렬은 항상 크기를 절반으로 쪼개서, 크기가 1일 때까지 쪼개고, 각 배열을 합쳐가면서 정렬을 수행하는 정렬 알고리즘이다. 
# 항상 절반으로 줄이기 때문에 logN의 레벨이 생기고, 각 레벨에서 N번 비교를 통해 배열을 병합하는 과정을 수행하기 때문에 O(nlgn) 시간 복잡도를 갖는다.

def merge_sort(array) :

    if len(array) == 1 :
        return array
    
    # (pl + pr) // 2 -> pl은 항상 0이기 때문에 pr을 2로 나누고 내림함
    mid = (len(array) - 1) // 2

    left = merge_sort(array[:mid + 1])
    right = merge_sort(array[mid + 1:])

    left_index = 0
    right_index = 0     

    result_list = []
    while left_index < len(left) and right_index < len(right) :
        if left[left_index] < right[right_index] :
            result_list.append(left[left_index])
            left_index += 1
        else :
            result_list.append(right[right_index])
            right_index += 1
    
    result_list.extend(left[left_index:])
    result_list.extend(right[right_index:])

    return result_list

print(merge_sort(array1))
print(merge_sort(array2))
print(merge_sort(array3))
print()
print()

# 계수 정렬 
# 계수 정렬이란 자연수의 값을 다루고 가장 작은 값과 가장 큰 값의 차이가 100만이 넘지 않으면 정렬을 O(N+K) 시간을 보장하는 정렬 알고리즘 N은 원소 개수, K는 최소값 최대값 차이이다. 

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def sort(array) :
    max_value = max(array)

    sort_table = [0] * (max_value + 1)

    for index in array :
        sort_table[index] += 1
    
    for num in range(len(sort_table)) :
        if sort_table[num] != 0 :
            for i in range(sort_table[num]) :
                print(num, end= " ")

sort(array)