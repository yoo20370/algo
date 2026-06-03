import sys

def solution(N, topList) :
    result = [0] * N

    stack = []
    
    

N = int(sys.stdin.readline().rstrip())

topList = list(map(int, sys.stdin.readline().split()))

result = solution(N, topList)

for i in result :
    print(i, end=" ")


