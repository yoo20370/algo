N = int(input())

coin = [25, 10, 5, 1]

for i in range(N) :
    money = int(input())

    for i in coin :
        T = money // i
        money = money % i 
        print(T, end=" ")
    print() 