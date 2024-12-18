import sys 

N = int(sys.stdin.readline().rstrip())

arr = list()
for _ in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse = True)

for data in arr :
    print(data, end=" ")