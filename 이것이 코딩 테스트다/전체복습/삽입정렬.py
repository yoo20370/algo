import sys

arr = [1,3,2,6,5,4,9,8,0]

# for i in range(1, len(arr)) :
#     insert_data = arr[i]
#     insert_idx = i
#     for j in range(i, 0, -1) :
#         if arr[j-1] > insert_data :
#            arr[j] = arr[j-1]
#            insert_idx = j - 1
#     arr[insert_idx] = insert_data

for select_idx in range(1, len(arr)) :
    for check_idx in range(select_idx, 0, -1) :
        if arr[check_idx - 1] > arr[check_idx] :
            arr[check_idx - 1], arr[check_idx] = arr[check_idx], arr[check_idx-1] 
        else :
            break

print(arr)