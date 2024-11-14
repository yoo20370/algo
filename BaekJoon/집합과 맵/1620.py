# import sys

# N, M = map(int, input().split())

# listA = [[] for _ in range(1000)]
# listB = [[] for _ in range(1000)]

# for i in range(1, N+1) :
#     data = sys.stdin.readline().rstrip()

#     hashVal = int(i) % 1000
#     hashVal2 = hash(data) % 1000

#     listA[hashVal].append([i, data])
#     listB[hashVal2].append([i, data])


# result = list()
# def func(hashTable, data, n) :
#     # 숫자인 경우
#     if n == 0 :
#         hashVal = int(data) % 1000
#         for i in hashTable[hashVal] :
#             if int(i[0]) == int(data) :
#                 result.append(i[1])
#     else :
#         hashVal = hash(data) % 1000
#         for i in hashTable[hashVal] :
#             if i[1] == data :
#                 result.append(i[0])

# for i in range(M) :
#     data = sys.stdin.readline().rstrip()
#     if data.isdigit() :
#         func(listA, data, 0)
#     else :
#         func(listB, data, 1)

# for i in result :
#     print(i)
import sys 
N, M = map(int, sys.stdin.readline().split())

dic = dict()

for i in range(1, N+1) :
    data = sys.stdin.readline().rstrip()
    dic[i] = data
    dic[data] = i

for i in range(M) :
    data = sys.stdin.readline().rstrip()
    if data.isdigit() :
        print(dic[int(data)])
    else :
        print(dic[data])


# 딕셔너리, sys 사용 
## 포켓몬 도감 완성하기
## 딕셔너리, sys 사용
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().strip().split())
# poketmon = dict()
# rvs_poketmon = dict()
# m_lst = []

# for i in range(1, n+m+1):
#     value = input().strip()
#     if i <= n:
#         poketmon[i] = value
#         rvs_poketmon[value] = i
#     else:
#         m_lst.append(value)
        
# for word in m_lst:
#     if word.isdigit():
#         print(poketmon[int(word)])
#     else:
#         print(rvs_poketmon[word])

#
# import sys

# n, m = map(int, sys.stdin.readline().split())
# dic={}

# for i in range(1, n+1):
#     a = sys.stdin.readline().rstrip()
#     dic[i] = a
#     dic[a] = i

# for i in range(m):
#     quest = sys.stdin.readline().rstrip()
#     if quest.isdigit():
#         print(dic[int(quest)])
#     else:
#         print(dic[quest])
