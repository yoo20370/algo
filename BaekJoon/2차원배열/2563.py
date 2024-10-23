N = int(input())

pan = [[0] * 100 for _ in range(100)]  


for i in range(N) :
    x, y = map(int, input().split())
    
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            pan[i][j] = 1

cnt = 0
for i in range(100) :
    cnt += pan[i].count(1)

print(cnt)