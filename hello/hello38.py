# 문자열 뒤집기 
# 모든 문자가 동일한 문자가 되도록 하려면 몇 번 뒤집어야 하는가
# 같은 숫자가 연속적인 것은 한 번에 뒤집을 수 있다. 

# 어떻게 카운트해야 하는가 ?? 
# 서로 다른 값이 될 때, 개수를 세면 될 것 같음 
# 예를 들어 0에서 1로 변경되는 구간은 0입장에서 1을 0으로 바꿔야 함 
# 반대로 1에서 0으로 바뀌는 구간은 1 입장에서 0을 1로 바꿔야 함 
# 또한 시작값의 경우는 처리할 수 없으므로 0인 경우 1입 장에서 1로 바꿔야 하므로 1 기준값을 증가시켜주면 될 것 같다.

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    first = string[0]

    # 1에서 0으로 변경된 개수 
    changeZeroCount = 0

    # 0에서 1로 변경된 개수 
    changeOneCount = 0

    # 0에서 1로 바뀌어야 하므로 
    if first == '0' :
        changeOneCount += 1
    else :
        # 1에서 0으로 바뀌어야 하므로 
        changeZeroCount += 1

    preNumber = first
    for index in range(1, len(string)) :

        # 연속된 숫자가 아닌 서로 다른 숫자가 나왔을 때 
        if preNumber != string[index] : 
            
            if string[index] == '0' :
                changeOneCount += 1
            else :
                changeZeroCount += 1
            
            # 값이 다르기 때문에 이전 문자 갱신 
            preNumber = string[index]


    return min(changeOneCount, changeZeroCount)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)