
def primeNumberSieve(n) :

    array = [True] * (n + 1) 

    array[0] = False
    array[1] = False 

    for i in range(2, int(n ** 0.5) + 1) :

        if array[i] == True :

            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(1, len(array)) :
        if array[i] :
            print(i, end = " ")
    

primeNumberSieve(100)