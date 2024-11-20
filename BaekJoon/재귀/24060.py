

# def merge_sort(arr) :

#     if len(arr) == 1 :
#         return arr
    
#     pl = 0
#     pr = len(arr) - 1
#     mid = len(arr) // 2

#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     l_idx = 0
#     r_idx = 0
    
#     resultList = list()
#     while l_idx < len(left) and r_idx < len(right) : 

#         if left[l_idx] < right[r_idx] :
#             resultList.append(left[l_idx])
#             l_idx += 1

#         else :
#             resultList.append(right[r_idx])
#             r_idx += 1
    
#     resultList.extend(left[l_idx:])
#     resultList.extend(right[r_idx:])
    
#     return resultList

def merge(arr, p, q, r) :
    i = p
    j = q
    t = 1

    while i <= q and j <= r :
        if arr[i] <= arr[j] :
            arr[t], arr[i] = arr[i], arr[t]
            t += 1
            i += 1
        else :
            arr[t], arr[j] = arr[j], arr[t]
            t += 1
            j += 1
    while i <= q :
        arr[t], arr[i] = arr[i], arr[t]
        t += 1
        i += 1
    while j <= r :
        arr[t], arr[j] = arr[j], arr[t]
        t += 1
        j += 1
    while i <= r :
        arr[i], arr[t] = arr[t], arr[i]
        i += 1
        j += 1

def merge_sort(arr, left, right) :
    pl = left
    pr = right

    if pl < pr :
        mid = (pl + pr) // 2
        merge_sort(arr, pl, mid) 
        merge_sort(arr, mid + 1, pr)
        merge(arr, pl, mid, pr)


arr = [4,2,3,1]

merge_sort(arr, 0, len(arr)-1)
print(arr)