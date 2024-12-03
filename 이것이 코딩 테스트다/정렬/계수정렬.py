
def sort(arr) :
    cnt = [0] *(max(arr) + 1)

    
    for i in arr :
        cnt[i] += 1

    for i in range(len(cnt)) :
        for _ in range(cnt[i]) :
            print(i, end=" ")


sort([3,3,2,4,1])