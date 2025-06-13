import sys

count = int(sys.stdin.readline().rstrip())

array = []
for _ in range(count) :
    array.append(int(sys.stdin.readline().rstrip()))

array.sort(reverse=True)

for number in array :
    print(number, end=" ")