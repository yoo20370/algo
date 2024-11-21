import sys 

N = sys.stdin.readline().rstrip()
listA = list(map(int, sys.stdin.readline().split()))

listA.sort()
result = 0
waitTime = 0 
for i in listA :
    result = result + waitTime + i 
    waitTime = waitTime + i

print(result)