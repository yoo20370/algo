# 좋은 접근 방식이지만 메모리 절약을 못함 
# input = "011110"

# # O(2N + 4) -> O(N)
# def find_count_to_turn_out_to_all_zero_or_all_one(string) -> int :
    
#     commpressed_string = [] # O(1)
#     # string 우선 압축해준다. 00011000 -> 010, 01010101010 -> 01010101010 # O(N) 
#     for char in string :
#         if not commpressed_string or commpressed_string[-1] != int(char) : # O(1)
#             commpressed_string.append(int(char))    # O(1)
    
#     compressed_string_length = len(commpressed_string) # O(1)

#     # 압축된 길이에서 sum()을 뺀다. 이 때, 이 때 결과가 압축된 길이보다 길면 0이 더 많은 것, 
#     # 문자열 길이 빼기 1의 개수 = 0의 개수 
#     zero_count = compressed_string_length - sum(commpressed_string) # O(1)

#     if zero_count <= compressed_string_length - zero_count : # O(1)
#         return zero_count   #O(1)
#     else : 
#         return compressed_string_length - zero_count

# result = find_count_to_turn_out_to_all_zero_or_all_one(input)
# print(result)

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    pre_char = string[0]
    zero_count = 1 if pre_char == '0' else 0
    one_count = 1 if pre_char == '1' else 0

    for char in string[1:] :
            
        if pre_char != char :
            if pre_char == '0' :
                zero_count += 1
            else :
                one_count += 1
        
        pre_char = char

    # 이 부분을 채워보세요!
    return min(zero_count, one_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 0애서 1을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
# 1애서 0을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업