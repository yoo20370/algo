N = int(input())

def func(n) :
    if n == 1 :
        return 0
    min = 1000001
    
    for i in range(1, n) :
        temp = 0
        for j in str(i) :
            temp += int(j)
        # N 구하기 
        if i + temp == n :
            # N의 생성자 중 최소값보다 작은 값인지 체크 
            if min > i + temp :
                min = i
    
    if min == 1000001 :
        return 0
    else :
        return min
    
print(func(N))



n = int(input())

for i in range(n):
    s = i
    r = i
    while i > 0:
        r += i % 10
        i = i // 10
    if r == n:
        print(s)
        break
else:
    print(0)