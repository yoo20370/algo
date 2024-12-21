import sys

arr = list(sys.stdin.readline().rstrip())

sumVal = 0
for item in arr :
    if sumVal == 0 or int(item) <= 1 :
        sumVal += int(item)
    else :
        sumVal *= int(item)

print(sumVal)