# N 바구니 개수
# M
N, M = map(int, input().split())

basket = [0] * N

for i in range(M) :
    S, E, B = map(int, input().split())

    S -= 1
    E -= 1
    for i in range(S,E+1,1):
        basket[i] = B
    
for i in basket :
    print(i, end=" ")
