import sys

K, N = map(int, sys.stdin.readline().split())

ls = list()

for _ in range(K) :
    ls.append(int(sys.stdin.readline().rstrip()))

max_length = max(ls)

start = 1
end = max_length
result = 0

while start <= end :
    curr_length = (start + end) // 2

    total_count = 0 
    for l in ls :
        total_count += l // curr_length
    
    if total_count < N :
        end = curr_length - 1
    elif total_count >= N :
        start = curr_length + 1 
        result = curr_length

print(result)
    
