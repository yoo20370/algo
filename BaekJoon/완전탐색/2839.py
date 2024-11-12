N = int(input())


def func(n) :
    # 3kg 개수 
    a = 0

    # 3의 개수가 최대임에도 불구하고 값을 정확히 맞추지 못하면 
    while a * 3 <= n : 
        r = n - a * 3 
        
        result = r // 5 
        if r % 5 != 0 :
            a += 1
        else :
            print(result + a)
            return 
    print(-1)

func(N)