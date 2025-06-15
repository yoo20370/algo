import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

yose_list = [i for i in range(1, N + 1)]

yose_list = deque(yose_list)

result_list = []
while yose_list :

    for _ in range(K - 1) :
        temp = yose_list.popleft()
        yose_list.append(temp)
    result_list.append(yose_list.popleft())

print("<", ", ".join(map(str, result_list)), ">", sep="")



