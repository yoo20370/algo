arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]

def select_sort(arr) :

    for select_idx in range(len(arr)-1) :
        min_idx = select_idx
        for compare_idx in range(select_idx + 1, len(arr)) :
            if arr[min_idx] > arr[compare_idx] :
                min_idx = compare_idx
        
        arr[select_idx], arr[min_idx] = arr[min_idx], arr[select_idx] 

select_sort(arr)
print(arr)