# 1차시도 -> 모두 시간초과
# 해시 테이블 실패, 
# import sys

# hashTable = [[] for i in range(100000)]

# N = sys.stdin.readline().rstrip()

# for i in list(map(int, sys.stdin.readline().split())) :
#     hashVal = i % 100000
#     hashTable[hashVal].append(i)

# M = sys.stdin.readline().rstrip()
# for i in list(map(int, sys.stdin.readline().split())) :
#     hashVal = i % 100000
#     print(hashTable[hashVal].count(i))    

# 2차시도 - 이분탐색 
import sys

# def binarySearch(dic, key) :
#     pl = 0 
#     pr = len(dic) - 1

#     while pl <= pr :
#         mid = (pl + pr) // 2
#         if 


N = sys.stdin.readline().rstrip()
dic = dict()

for i in list(map(int, sys.stdin.readline().split())) :
    if dic.get(i) :
        x = dic.get(i)
        x = x + 1
        dic[i] = x
    else :
        dic[i] = 1

M = sys.stdin.readline().rstrip()
for i in list(map(int, sys.stdin.readline().split())) :
    if dic.get(i) :
        print(dic.get(i), end=" ")
    else :
        print(0, end=" ")





