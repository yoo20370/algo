array = [1, 2, 3, 2, 5]

# def two_pointer(numbers, m) -> int :

#     start_index = 0
#     end_index = 0

#     sum_match_count = 0
#     while start_index < len(numbers) and end_index < len(numbers) :

#         # 우선 구간의 값을 더해서 총합을 구한다.
#         # 총합이 m보다 작다면 end_index를 1 증가시킨다.
#         # 총합이 같거나 크가면 start_index를 1 증가시킨다.
#         curr_sum = 0
#         for curr_index in range(start_index, end_index + 1) :
#             curr_sum += numbers[curr_index]
        
#         # 일치하는 경우 
#         if curr_sum == m :
#             sum_match_count += 1
#             start_index += 1
#         elif curr_sum > m :
#             # 값이 크거나 같은 경우 범위를 줄여 값을 감소시킨다.
#             start_index += 1
#         else :
#             # 값이 작은 경우 범위를 늘려 값을 증가시킨다.
#             end_index += 1

#     return sum_match_count

def two_pointer(numbers, m) -> int :

    
    curr_sum = 0
    end_index = 0
    sum_match_count = 0

    for start_index in range(len(numbers)) :

        while curr_sum < m and end_index < len(numbers) :
            curr_sum += numbers[end_index]
            end_index += 1 
        
        if curr_sum == m :
            sum_match_count += 1
        curr_sum -= numbers[start_index]
    return sum_match_count

result = two_pointer(array, 5)
print(result)
