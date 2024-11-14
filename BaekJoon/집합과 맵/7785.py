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

## set은 remove가 빠르다. 반면 list는 remove가 느리다.
## -> remove는 제거 후 순서를 조정해줘야 함 