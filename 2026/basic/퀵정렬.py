input = [4, 6, 2, 9, 1]

# 퀵정렬은 피벗을 기준으로 이동시켜야 하는 원소를 찾아서 이동시키고 이를 피벗을 기준으로 계속 배열을 쪼개가며 수행하는 알고리즘이다. 


def quick_sort(array, left, right):

    pl = left
    pr = right
    p = array[(left + right) // 2]

    # <= 인 이유는 pl과 pr이 둘 다 동일한 원소를 가리킬 수 있음 
    while pl <= pr :

        while array[pl] < p :
            pl += 1
        
        while array[pr] > p : 
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
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",quick_sort([100,56,-3,32,44], 0, len([100,56,-3,32,44]) - 1))