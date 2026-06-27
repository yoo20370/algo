import sys


N, M = map(int, sys.stdin.readline().split())

dic = dict()
listA = list()
for i in range(N) :
    data = sys.stdin.readline().rstrip()
    if len(data) < M :
        continue
    if dic.get(data) :
        x = dic.get(data) 
        dic[data] = x + 1
    else :
        dic[data] = 1

listA = list()
for x,y in dic.items() :
    listA.append([y, len(x), x])

listA.sort(key = lambda x :(-x[0],-x[1], x[2]))

for x,y,z in listA :
    print(z)
