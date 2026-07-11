# 곱하기 혹은 더하기
# 각 자리가 0부터 9로만 이루어진 문자열 S가 주어졌을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 X 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 만들어라 
import sys

def solution() :
    inputData = sys.stdin.readline().rstrip()

    totalSum = 0 
    for number in inputData :
        number = int(number)
        if totalSum <= 1 or number <= 1 :
            totalSum += number 
        else :
            totalSum *= number 

    return totalSum

result = solution()
print(result)