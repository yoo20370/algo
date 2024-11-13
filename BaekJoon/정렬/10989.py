import sys 

listA = [0] * 10001

N = int(sys.stdin.readline())

for i in range(N) :
    data = int(sys.stdin.readline())
    listA[data] += 1

for i in range(1, 10001) :
    if listA[i] != 0 :
        for _ in range(listA[i]) :
            print(i)