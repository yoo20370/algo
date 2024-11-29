## 최대 O(N) 시간 복잡도 

# import sys

# N, M, K = map(int, sys.stdin.readline().split())

# arr = list(map(int, sys.stdin.readline().split()))

# arr.sort(reverse=True)

# def func(N, M, K) :

#     cnt = 0 
#     sum = 0
#     if arr[0] == arr[1] :
#         return M * arr[0]

#     while M != 0 :
#         if M >= K and cnt != K : 
#             sum += arr[0] * K
#             M -= K
#             cnt = K
#             continue
#         elif cnt != K :
#             sum += arr[0]
#             cnt += 1
#         else :
#             sum += arr[1]
#             cnt = 0 
#         M -= 1
    
#     print(sum)

# func(N,M,K)

## 상수 시간 O(1) 시간 복잡도 
import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

def func(n, m, k) :
    result = 0 
    val = m // (k+1) 
    remain = m % (k+1)

    print(val, remain)
    result = (arr[0] * K + arr[1]) * val

    result += remain * arr[0]

    print(result)

func(N,M,K)

