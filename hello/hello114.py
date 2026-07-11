# 문자열 재정렬 
# 알파벳 대문자와 숫자 0 ~ 9로 구성된 문자열이 입력으로 주어짐
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 모든 숫자를 더한 값을 이어서 출력한다. 
# 가장 먼저 떠오른 방법 
# 순회를 통해서 문자와 숫자를 구분한다. 
# 문자를 정렬하고, 숫자는 합한다.

import sys 

def solution() :
    inputDatas = sys.stdin.readline().rstrip()

    alphabetList = []
    numberSum = 0
    numberCount = 0 
    for currentData in inputDatas :
        if currentData.isalpha() :
            alphabetList.append(currentData)
        else :
            numberSum += int(currentData)
            numberCount += 1

    sortedString = sorted(alphabetList)

    if numberCount == 0 :
        numberSum = ""

    return "".join(sortedString) + str(numberSum)

result = solution()
print(result)