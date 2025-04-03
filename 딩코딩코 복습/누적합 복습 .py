n = 5
data = [10, 20, 30, 40, 50]

prefix = [0 for i in range(n + 1)]

prefix_sum = 0

for i in range(1, n + 1) :
    prefix_sum += data[i - 1]
    prefix[i] = prefix_sum

print(prefix[5] - prefix[3])