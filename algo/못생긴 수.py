import sys 
# 여기서 핵심은 2, 3, 5를 가지고 놀아야 한다는 것 
def solution() :

    n = int(sys.stdin.readline().rstrip())

    memo = [0] * n
    memo[0] = 1

    i2, i3, i5 = 0, 0, 0

    next2, next3, next5 = 2, 3, 5 

    for l in range(1, n) :

        memo[l] = min(next2, next3, next5)

        if memo[l] == next2 :
            i2 += 1
            next2 = memo[i2] * 2
        if memo[l] == next3 :
            i3 += 1
            next3 = memo[i3] * 3
        if memo[l] == next5 :
            i5 += 1
            next5 = memo[i5] * 5
            
    print(memo[n-1])

    

solution()
