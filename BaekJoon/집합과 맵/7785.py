import sys 

N = int(input())


setA = set()
for i in range(N) :
    x, y = sys.stdin.readline().split()
    if y == 'leave':
        setA.remove(x)
    else :
        setA.add(x)

listA = list()
for i in setA :
    listA.append(i)
listA.sort(reverse=True)

for i in listA :
    print(i)