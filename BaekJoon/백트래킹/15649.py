# import sys
# N, M = map(int, sys.stdin.readline().split())


# check = [False] * N
# # 열의 길이는 m, 행의 길이는 N 
# def func(n, m, cnt, check, arr) :
#     if m <= cnt  :
#         for i in arr :
#             print(i+1, end=" ")
#         print()
#         return 
    
#     for i in range(N) :
#         if check[i] == False :
#             check[i] = True 
#             print(check)
#             arr.append(i)
#             func(n, m, cnt+1, check, arr)
#             arr.pop()
#             check[i] = False 
    
# func(N, M, 0, check, list())
    



## 다른 사람 풀이
# import sys
# N, M = map(int, sys.stdin.readline().split())
# print = sys.stdout.write


# def progression(n, m, sequence=[]):
#     if len(sequence) == m:
#         print(' '.join(map(str, sequence))+'\n')
#         return

#     for i in range(1, n+1):
#         if i not in sequence:
#             progression(n, m, sequence + [i])
    
# progression(N, M)


## 다른 사람 풀이
# N, M = map(int, input().split())
# seq = []
# for _ in range(M) :
#     seq.append('')

# def sequence(num) :
#     if (check(num) == True) :
#         if (num == M) :
#             print(*seq)
#         else :
#             for i in range(1, N + 1) :
#                 seq[num] = i
#                 sequence(num + 1)
# def check(num) :
#     for i in range(0, num - 1) :
#         if (seq[i] == seq[num - 1]) :
#             return False
#     return True

# sequence(0)