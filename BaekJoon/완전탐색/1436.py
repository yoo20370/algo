N = int(input())


def func() :
    start = 666 
    cnt = 0
    while True : 
        if '666' in str(start) :
            cnt += 1

        if cnt == N :
            print(start)
            return
    
        start += 1
        
func()