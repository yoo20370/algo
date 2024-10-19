T = 30
S = 28

stuList = [False] * T
for i in range(S) :
    N = int(input())
    stuList[N-1] = True

for i in range(T) :
    if stuList[i] == False :
        print(i+1)
        

