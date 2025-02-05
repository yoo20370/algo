# def find_max_num(array):

#     max_idx = 0

#     for idx in range(1, len(array)) :
#         if array[max_idx] < array[idx] :    max_idx = idx 


#     return array[max_idx]


# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# def find_max_occurred_alphabet(string):

    
#     data_store = [0] * 26

#     offset = ord("a")

#     for ch in string :
#         if ch.isalpha() :
#             data_store[ord(ch) - offset] += 1 

#     max_idx = 0
#     for idx in range(1, len(data_store)) :
#         if data_store[max_idx] < data_store[idx] :
#             max_idx = idx


#     result = chr(max_idx + offset)
#     return result

# result = find_max_occurred_alphabet
# print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# def is_number_exist(number, array):
#     # 배열을 순회하면서 number와 같은 것이 있으면 True 반환 없으면 False 반환 
#     for curr in array :
#         if number == curr :
#             return True 

#     return False


# result = is_number_exist
# print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
# print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
# print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

# def find_max_plus_or_multiply(array):
#     # 배열을 순회하면서 현재 값이 0이거나 1이거나 혹은 전체합이 1이하인 경우 더하고 나머지는 곱하겠다.
#     total = 0 # 1
#     for curr in array :  # N 
#         if curr <= 1 or total <= 1: # 1 
#             total += curr  # 1
#         else :
#             total *= curr # 1
#     return total


# result = find_max_plus_or_multiply
# print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
# print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
# print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

input = "abadabac"

def find_not_repeating_first_character(string):
    
    alphabet_cnt = [0] * 26

    for char in string :
        if char.isalpha() :
            alpha_idx = ord(char) - ord('a')
        alphabet_cnt[alpha_idx] += 1


    not_reapeat_char = []
    for idx in range(len(alphabet_cnt)) :
        if alphabet_cnt[idx] == 1 :
            not_reapeat_char.append(chr(idx + ord('a')) )
    
    for char in string :
        for not_char in not_reapeat_char :
            if char == not_char :
                return char

    return "_" 
        


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))