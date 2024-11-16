while True:
    N = int(input())

    if N == -1 :
        break
    
    dataList = set()
    for i in range(1, N+2 // 2) :
        if N % i == 0 :
            dataList.add(i)
            dataList.add(N // i)

    dataList = sorted(dataList)
    sum = 0
    for i in dataList :
        if i != N :
            sum += i
    
    if sum == i :
        print(N, "=", end=" ")
        for i in range(len(dataList)-1) :

            print(dataList[i], end=" ")
            if len(dataList) - 2 != i :
                print("+", end=" ")
                
    else : 
        print(N, "is NOT perfect.")


# while 1:
#     n = int(input())
#     if n == -1:
#         break
#     lst = []
#     for i in range(1, n):
#         if n % i == 0 :
#             lst.append(i)
#     if sum(lst) == n:
#         ans = f"{n} = "
#         for item in lst:
#             ans += f"{item} + "
#         print (ans[:-2])
#     else:
#         print(f"{n} is NOT perfect.")

# def cx(n):
#     cnt = 1
#     arr = []
#     target = 0

#     for i in range(1,n):
#         if n % i == 0:
#             arr.append(i)

#     arr.sort()
#     s = ' + '.join(map(str, arr))

#     if sum(arr) != n:
#         print(f'{n} is NOT perfect.')
#     else:
#         print(f'{n} = {s}')


# while 1:
#     n = int(input())

#     if n == -1:
#         break
#     else:
#         cx(n)
