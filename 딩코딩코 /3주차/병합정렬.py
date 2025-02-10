array = [4, 2, 3, 1, 0, 5]


def merge_sort(array) :

    # 병합 정렬이란 우선 배열을 크기가 1이될 때까지 나눈다. 재귀를 통해 나눈다.
    # 크기가 1인 것들 부터 비교하면서 크기가 작은 것부터 결과 배열에 넣는다. 이를 원래 배열의 크기가 될 때까지 반복한다.
    # 병합 정렬의 종료 조건은 배열의 길이가 1이될 때까지 
    # 문제 축소는 배열의 크기가 줄어드는 것 

    if len(array) <= 1 :
        return array
    
    pl = 0
    pr = len(array) - 1
    mid = (pl + pr) // 2

    # 리스트 슬라이싱은 start:end에서 end는 포함하지 않으므로 +1을 해줘야 정확히 절반으로 잘린다. 
    # 궁극적으로 [] 리스트가 되면서 무한루프에 빠지게 됨 
    left_array = merge_sort(array[pl:mid+1])
    right_array = merge_sort(array[mid+1:])

    result_list = []

    left_index = 0
    right_index = 0
    while left_index < len(left_array) and right_index < len(right_array) :

        if left_array[left_index] <= right_array[right_index] :
            result_list.append(left_array[left_index])
            left_index += 1
        else :
            result_list.append(right_array[right_index]) 
            right_index += 1

    result_list.extend(left_array[left_index:])
    result_list.extend(right_array[right_index:])

    return result_list

print(merge_sort(array))



