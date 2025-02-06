array = [10, 20, 30, 40, 50]

curr_sum = 0

p = [0]
for i in range(len(array)) :

    curr_sum += array[i]
    p.append(curr_sum)

print(p)

left = 3
right = 4

print(p[right] - p[left-1])