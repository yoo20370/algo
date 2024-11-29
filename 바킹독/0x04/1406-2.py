import sys

listA = list()

inputData = list(sys.stdin.readline().rstrip())

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    command = sys.stdin.readline().split()

    if command[0] == "L" :
        if len(inputData) != 0 :
            listA.append(inputData.pop())
    elif command[0] == "D" :
        if len(listA) != 0 :
            inputData.append(listA.pop())
    elif command[0] == "B" :
        if len(inputData) != 0 :
            inputData.pop()
    elif command[0] == "P" :
        inputData.append(command[1])

j = len(listA)
for i in  range(j):
    inputData.append(listA.pop())

for i in inputData :
    print(i,end="")