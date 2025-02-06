import sys 

start_number, end_number = map(int, sys.stdin.readline().split())

prime_array = [True] * (end_number + 1)


for i in range(2, int(end_number ** 0.5) +1) :

    if prime_array[i] == True :

        j = 2
        while i * j <= end_number :
            prime_array[i * j] = False
            j += 1


for curr_index in range(start_number, end_number+1) :

    if prime_array[curr_index] :
        print(curr_index)




        