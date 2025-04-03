input = "01010101"

# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     # 문자열을 순회하면서 0과 1의 뒤집는 개수를 센다.
#     # 0으로 시작하는 경우 0에서 1로 바뀌는 순간에 0의 count를 올려주고
#     # 1로 시작하는 경우 1에서 0으로 바뀌는 순간에 1의 count를 올려준다.
#     # 만약 0이거나 1일 때, 끝에 도달한 경우도 올려준다. 
#     # 0인 경우 순회하면서 1이 나타날 때까지 이동, 1이 나타나면 

#     zero_count = 0
#     one_count = 0

#     curr = string[0]
#     for ch in string[1:]:
#         if curr != ch :
#             if curr == '0' : zero_count += 1
#             else : one_count += 1
#             curr = ch

#     if curr == '0' : zero_count += 1
#     else : one_count += 1
    
#     return min(zero_count, one_count)

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    zero_count = 0
    one_count = 0

    curr = string[0]

    if curr == '0' :
        zero_count += 1
    else :
        one_count += 1
    
    for ch in string[1:] :
        if ch != curr :
            if ch == '0' :
                zero_count += 1
            else :
                one_count += 1
            curr = ch
    
    return min(zero_count, one_count)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)