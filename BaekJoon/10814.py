N = int(input())

listA = list()

for i in range(N) :
    num, name = input().split()
    listA.append([int(num), name])

listA.sort(key = lambda x : x[0])

for a, b in listA :
    print(a, b)