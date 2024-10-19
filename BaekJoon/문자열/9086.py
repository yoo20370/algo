N = int(input())

outputString = ""
for i in range(N) :
    inputString = input()
    length = len(inputString)
    outputString += inputString[0]
    outputString += inputString[length - 1] + "\n"
print(outputString)