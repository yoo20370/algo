# N = int(input())

# # 소인수 체크 
# def func2(n) :
#     if n == 2 or n == 3 or n == 5:
#         return True
#     if n % 2 == 0 :
#         return False 
#     for i in range(3, n, 2) :
#         if n % i == 0 :
#             return False
#     return True

# # 약수 구하기 (인수)
# def func(n) :
#     listA  = list()
#     for i in range(2, n+1) :
#         # 약수 체크
#         if n % i == 0 :
#             if func2(i) == True :
#                 listA.append(i)
#     return listA


# listA = func(N)

# def func3(n, listA) :
#     resultList = list()


#     s = 0
#     i = listA[s]
#     while  n / i != 1 :
#         if n % i != 0 :
#             s += 1
#             i = listA[s]        
#         elif n % i == 0 :
#             resultList.append(i)
#             n = int(n / i)
        
#     resultList.append(i)
#     return resultList

# if N == 1 :
#     print("")
# else : 
#     listA = func3(N, listA)
#     for i in listA :
#         print(i)

N = int(input())

def func(n) :
    if n == 1 :
        print("")
        return 

    while n != 1 :
        for i in range(2, (n + 1 // 2)) :
            if n % i == 0 :
                print(i)
                n = int(n / i)
                break
func(N)