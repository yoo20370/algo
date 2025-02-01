import sys

def insert_sort(arr) :

    for i in range(1, len(arr)) :
        j = i

        while j > 0 and arr[j-1] < arr[j] :
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

arr = list()

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

insert_sort(arr)
print(arr)