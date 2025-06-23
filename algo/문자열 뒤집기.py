# 처음 숫자가 뭔지 확인하고, 그 숫자가 뭔지에 따라 카운트
# 그리고 순회하면서 현재 숫자에서 다른 숫자로 바뀌는 것을 카운트한다. -> 0에서 1로 바뀌면 1로 카운트 
import sys 

def solution() :

    string = sys.stdin.readline().rstrip() 

    zero_count = 0
    one_count = 0

    if string[0] == "1" :
        one_count += 1
        sequence_number = "1"
    else :
        zero_count += 1
        sequence_number = "0"

    for char in string :
        # 연속적인 숫자가 아니고, 그 숫자가 1이라면 
        if char != sequence_number and char == "1":
            one_count += 1
            sequence_number = "1"
        elif char != sequence_number and char == "0":
            zero_count += 1
            sequence_number = "0"

    return min(zero_count, one_count)

print(solution())