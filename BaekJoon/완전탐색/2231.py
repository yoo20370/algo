# N = int(input())

# def func(n) :
#     if n == 1 :
#         return 0
#     min = 1000001

#     for i in range(1, n) :
#         temp = 0
#         for j in str(i) :
#             temp += int(j)
#         # N 구하기 
#         if i + temp == n :
#             # N의 생성자 중 최소값보다 작은 값인지 체크 
#             if min > i + temp :
#                 min = i
    
#     if min == 1000001 :
#         return 0
#     else :
#         return min
    
# print(func(N))

N = int(input())

def func(n) :
    if n == 1 :
        return 0
    min = 1000001

    for i in range(max(1, n - (len(str(n)) * 9)), n) :
        sumVal = sum(map(int, list(str(i))))
        if i + sumVal == n :
            if min > i + sumVal :
                min = i        
    
    if min == 1000001 :
        return 0
    else :
        return min
    
print(func(N))


# # 다른 사람 1
# n = int(input())

# for i in range(n):
#     s = i
#     r = i
#     while i > 0:
#         r += i % 10
#         i = i // 10
#     if r == n:
#         print(s)
#         break
# else:
#     print(0)

# # 다른 사람 2 - 당신 고트
# N = int(input())
# s = max(N - 63, 1)
# for n in range(s,N):
#     t = n + sum(map(int, str(n)))
#     if t == N:
#         print(n)
#         break
# else:
#     print(0)