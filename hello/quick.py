

def quick_sort(array, left, right):

    pl = left
    pr = right

    p = array[(left + right) // 2]

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
    if left < pr :
        quick_sort(array, left, pr)
    
    return array


print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",quick_sort([5,8,4,7,7], 0 , 4))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",quick_sort([3,-1,17,9], 0, 3))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",quick_sort([100,56,-3,32,44], 0 , 4))