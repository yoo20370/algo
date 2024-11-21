import sys 

N = sys.stdin.readline().rstrip()
listA = list(map(int, sys.stdin.readline().split()))

listA.sort()
result = 0
sum = 0 
for i in listA :
    sum = sum + i
    result = result + sum

print(result)