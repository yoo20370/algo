array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    # 병합정렬
    # 병합정렬은 항상 반으로 나누므로 깊이가 lgN이 되고, 각 높이에서 N번 비교해야 하므로 O(nlgN)시간 복잡도를 갖는다. 
    # 퀵정렬과 달리 항상 동일하게 나눠지기 때문에 항상 O(nlgN) 시간 복잡도를 보장한다.
    # 단, 추가적인 저장공간이 필요하므로 재자리 정렬이 아니고 안정정렬이다. 

    # 종료조건 - 쪼개진 배열이 크기가 1이면 종료시킨다.
    # 축소조건 - 항상 배열을 절반의 크기로 분할하고 이를 크기가 1일때까지 반복한다.
    # 병합하면서, 두 배열의 값을 비교하며 결과 배열을 만들고 결과 배열을 반환한다.

    if len(array) <= 1 :
        return array
    
    mid = (len(array) - 1) // 2

    # 
    left = merge_sort(array[:mid + 1])
    right = merge_sort(array[mid + 1:])

    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right) :
        if left[left_index] < right[right_index] :
            result.append(left[left_index])
            left_index += 1

        else :
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))