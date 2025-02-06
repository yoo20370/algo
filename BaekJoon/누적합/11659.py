import sys 

number_count, plus_count = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

p_sum = [0]
curr_sum = 0


for arr_index in range(len(array)) :

    curr_sum += array[arr_index]
    p_sum.append(curr_sum)

for _ in range(plus_count) :
    start_index, end_index = map(int, sys.stdin.readline().split())

    print(p_sum[end_index] - p_sum[start_index - 1])

