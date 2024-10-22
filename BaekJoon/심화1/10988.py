data = input()

def checkFunc(string) :

    length = len(string)
    for i in range(length // 2) :
        if string[i] != string[length - 1 - i] :
            return 0
    return 1

print(checkFunc(data))