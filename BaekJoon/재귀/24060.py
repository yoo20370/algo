import sys

def merge_sort(arr, pl, pr, tmp) :
    if pl < pr :
        p = (pl + pr) // 2
        merge_sort(arr, pl, p, tmp) 
        merge_sort(arr, p + 1, pr, tmp)
        merge(arr, pl, p, pr, tmp)

def merge(arr, pl, p, pr, temp) :
    i = pl 
    j = p + 1

    tmp = list()
    while i <= p and j <= pr :
        if arr[i] <= arr[j] :
            
            tmp.append(arr[i])
            i += 1
        else :
            
            tmp.append(arr[j])
            j += 1
    
    while i <= p :
        
        tmp.append(arr[i])
        i += 1
    
    while j <= pr :
        
        tmp.append(arr[j])
        j += 1
    i = pl
    t = 0
    
    while i <= pr :
        temp.append(tmp[t])
        arr[i] = tmp[t]
        t += 1
        i += 1

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

tmp = list()
merge_sort(arr, 0, len(arr) - 1, tmp)

if len(tmp) >= M :
    print(tmp[M-1])
else :
    print(-1)


