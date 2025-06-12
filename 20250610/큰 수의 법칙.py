import sys

array_length, add_count, K = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

# 우선 내림차순 정렬을 수행한다. 
# add_count를 K+1로 나눠 몫을 구한다. (K * 첫 번째 큰수 + 두 번째 큰 수) * 몫 + 나머지 * 첫 번째 큰 수 
array.sort(reverse=True)

first_number = array[0]
second_number = array[1]

sequence_number_count = add_count // (K+1) 
remain_count = add_count % (K+1)

result = (K * first_number + second_number) * sequence_number_count + (remain_count * first_number)

print(result)
