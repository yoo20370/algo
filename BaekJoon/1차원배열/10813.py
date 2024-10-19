N, M = map(int, input().split())

basket = [a for a in range(1,N+1)]

for i in range(M) :
    A, B = map(int, input().split())
    basket[A-1], basket[B-1] = basket[B-1], basket[A-1]

for i in basket :
    print(i, end=" ")