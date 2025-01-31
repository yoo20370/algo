arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
# arr = [4, 2, 3, 1]

def insert_sort(arr) :

    for i in range(1, len(arr)) :
        j = i 

        while j > 0 and arr[j-1] > arr[j] :
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1



insert_sort(arr)

print(arr)