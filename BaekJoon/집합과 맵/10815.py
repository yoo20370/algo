# 시간 초과 
# N = int(input())
# listA = list(map(int, input().split()))

# M = int(input())
# listB = list(map(int, input().split()))

# def func(i) :
#     for j in listA :
#         if i == j :
#             print(1, end =" ")
#             return
#     print(0, end =" ")
    
# for i in listB :
#     func(i)

def func(hashTable, hashVal, i) :
    hashVal = i % 10000
    for j in hashTable[hashVal] :
        if i == j :
            return 1
    return 0

import sys 

hashTable = [[] for i in range(10000)]

N = int(sys.stdin.readline().rstrip())
for i in list(map(int, sys.stdin.readline().split())) :
    hashVal = i % 10000
    hashTable[hashVal].append(i)

M = int(sys.stdin.readline().rstrip())
for i in list(map(int, sys.stdin.readline().split())) :
    hashVal = i % 10000
    print(func(hashTable, hashVal, i), end= " ")


    
