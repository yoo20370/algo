 
def solution(string):
    zeroCount = 0
    oneCount = 0 

    if string[0] == '0' :
        oneCount += 1
    else :
        zeroCount += 1

    for index in range(len(string)-1):
        if string[index] != string[index + 1] :
            if string[index + 1] == '0' :
                oneCount += 1
            else :
                zeroCount += 1

    return min(zeroCount, oneCount)

string = input()
print(solution(string))