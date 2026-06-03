# 안 나오는 것 까지 돌 필요 없음 
# 그러니 각각의 위치를 먼저 기록해버리자
# 만약 먼저 기록된 게 있다면 앞에 있는 거니까 무시하고 넘어간다. 

## 주어진 단어를 순회한다.
### 주어진 단어를 순회하면서 리스트에 위치를 기록한다. 
### 이때, -1이 아닌 경우 위치를 기록하지 않는다/
## 그냥 출력한다.
import sys

def solution(word) :
    alphaList = [-1] * 26

    for index in range(0, len(word)) :
        char = word[index]
        alphaIndex = ord(char) - ord('a')

        if alphaList[alphaIndex] == -1 :
            alphaList[alphaIndex] = index

    for value in alphaList :
        print(value, end = " ")


input = sys.stdin.readline().rstrip()

solution(input)
        

