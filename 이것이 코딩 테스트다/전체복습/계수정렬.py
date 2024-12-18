arr = [1,3,2,6,5,4,9,8,0]

array = [0] * (max(arr) + 1)

for data in arr :
    array[data] += 1

for idx in range(len(array)) :
    for _ in range(array[idx]) :
        print(idx, end=" ")

