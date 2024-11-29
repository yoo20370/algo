import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

def func(N, M, K) :

    cnt = 0 
    sum = 0
    if arr[0] == arr[1] :
        return M * arr[0]

    while M != 0 :
        if cnt != K :
            sum += arr[0]
            cnt += 1
        else :
            sum += arr[1]
            cnt = 0 
        M -= 1
    
    print(sum)

func(N,M,K)