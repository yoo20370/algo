input = [4, 6, 2, 9, 1]

def quick_sort(left, right, array):
    # 이 부분을 채워보세요!
    pl = left
    pr = right 
    p = array[(pl+pr)//2]

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
        quick_sort(pl, right, array)
    if left < pr :
        quick_sort(left, pr, array)

    return array

quick_sort(0, len(input) - 1, input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
