# 퀵 정렬 
# 피벗을 기준으로 두 포인터가 피벗보다 큰 값, 작은 값을 찾아서 Swap하고 
# 이 과정을 배열을 쪼개서 진행함
# 다만, 병합 정렬처럼 추가적인 공간을 사용해서 정렬하는 방식이 아니라 
# 인덱스를 이용해서 정해진 구간에 대해서 정렬하는 정렬 알고리즘
# 일반적으로 lgN으로 쪼개지고 총 N번의 비교를 수행하기 때문에 O(NlgN) 시간복잡도를 갖는다.
# 불안정 정렬, 제자리 정렬 
# 최악 O(N) -> 피벗 잘못 설정하는 경우 

data = [13, 4, 19, 1, 8, 16, 5, 11, 20, 3, 14, 7, 18, 10, 2, 15, 6, 17, 9, 12]

def quickSort(data, left, right) :

    pl = left 
    pr = right 

    # 인덱스로 다루게 되면 중간에 다른 QuickSort에 의해서 값이 변경될 수 있음 그래서 p라는 변수에 저장해서 기준을 결정 
    p = data[(pl + pr) // 2]

    while pl <= pr :

        # 기준 값보다 큰 값을 찾아라 
        while data[pl] < p :
            pl += 1
        
        # 기준 값보다 작은 값을 찾아라 
        while data[pr] > p :
            pr -= 1

        if pl <= pr :
            data[pl], data[pr] = data[pr], data[pl]
            # 처리 후 이동 -> 그러지 않으면 무한 루프 
            pl += 1
            pr -=1
    
    # 아직 끝에 도달하지 못했다면 
    if pl < right :
        quickSort(data, pl, right)
    
    if pr > left :
        quickSort(data, left, pr)



def solution() :

    quickSort(data, 0, len(data) - 1)

    print(data)


solution()