N = int(input())

def checkWord(string) :

    for i in range(len(string)- 1) :
        end = i
        for j in range(i+1, len(string)) :

            if string[i] != string[j] :
                end = j
            elif end != i :
                return 0

    return 1

ctn = 0
for i in range(N) :
    data = input()
    ctn += checkWord(data)

print(ctn)
