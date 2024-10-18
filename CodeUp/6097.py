H, W = map(int, input().split())

pan = [[0] * H for _ in range(W)]


## d가 0이면 세로 방향 막대, 1이면 가로 방향 막대
N = int(input())
inputList = list()
for i in range(N) :
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    xx = 0
    yy = 0 
    if d == 0 :
        yy = 1
    else :
        xx = 1
    
    for i in range(l) :
        pan[y + yy * (i)][x + xx * (i)] = 1


for i in range(H) :
    for j in range(W) :
        print(pan[j][i], end=" ")
    print()
