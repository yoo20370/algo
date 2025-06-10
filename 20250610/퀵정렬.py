input = [4, 6, 2, 9, 1]

def quick_sort(array, left, right):
    # 퀵 정렬, 
    # 퀵 정렬은 피봇을 이용해, 배열을 lgN 깊이로 분할하고 각 깊이에서 N번 비교를 통해 정렬을 수행하므로, O(NlgN) 시간 복잡도를 갖는다.
    # 퀵 정렬은 제자리 정렬, 불안정 정렬이며, 캐시 친화적이기 때문에 병합정렬보다 빠르다. 
    # 퀵 정렬은 피봇을 잘못 설정하면 O(N**2) 시간 복잡도를 가질 수 있다. 

    pl = left
    pr = right
    pivot = array[(pl + pr) // 2]

    while pl <= pr :
        while array[pl] < pivot :
            pl += 1

        while array[pr] > pivot :
            pr -= 1 

        if pl <= pr :
            array[pl], array[pr] = array[pr], array[pl] 
            pl += 1
            pr -= 1

    if pl < right :
        quick_sort(array, pl, right) 
    if pr > left : 
        quick_sort(array, left, pr)

    return array

quick_sort(input, 0, len(input) - 1)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",quick_sort([5,8,4,7,7], 0, len([5,8,4,7,7]) - 1))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",quick_sort([3,-1,17,9], 0, len([3,-1,17,9]) - 1))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",quick_sort([100,56,-3,32,44], 0, len([100,56,-3,32,44]) -1))