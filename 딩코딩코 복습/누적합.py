n = 5 
data = [10, 20, 30, 40, 50]

sum_value = 0 
prefix_sum = [0] * (n+1)

for i in range(1, n+1) :
    prefix_sum[i] = prefix_sum[i-1] + data[i-1]

def 구간합(start, end) :
    return prefix_sum[end] - prefix_sum[start - 1]

print(구간합(3, 4))