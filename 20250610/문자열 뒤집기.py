import sys

input = sys.stdin.readline().rstrip()

# 가독성이 조금 떨어지는 것 같음 
# 가독성 좋게 수정하는게 좋을 듯 

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 모두 1로 만들거나 모두 0으로 만들 수 있는 상황 
    # 현재 숫자를 기준으로 count 한다. 그리고 바뀔 때, 현재 숫자를 해당 숫자로 변경한다.

    count_array = [0] * 2 

    # 기존 숫자 설정
    number = string[0]
    count_array[int(number)] += 1

    # 문자열 순회 
    for curr_index in range(1, len(string)) :
        # 만약 기존 숫자와 다른 숫자라면, 다른 숫자를 기존 숫자로 변경하고 카운트한다. 
        if number != string[curr_index] :
            number = string[curr_index]
            count_array[int(number)] += 1

    return min(count_array)

    
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)