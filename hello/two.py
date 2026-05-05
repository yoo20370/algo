# 처음 접근을 어떻게 할 것이냐 ?? 
# 0에서 1로 바뀌거나 1에서 0으로 바뀌는 경우에 대해서 고민해야 할 것 같음 
# 두 가지 기준이 있음 0을 모두 1로 바꾸거나, 1을 모두 0으로 바꾸거나 
# 0으로 만드는 경우 -> 0에서 1으로 넘어가는 경우에 대해서 count
# 1로 만드는 경우 -> 1에서 0으로 넘어가는 경우에 대해서 count 

## 첫 숫자가 뭔지에 따라 시작 숫자가 다를 듯 
## 0으로 시작하면 1로 변경해야 하므로 1의 count + 1
## 1로 시작하면 0으로 변경해야 하므로 0의 count + 1

### string을 순회하면서 0에서 1로 바뀌는 지점과 1에서 0으로 바뀌는 지점에 대해서 count를 진행한다.
### 0에서 1로 바뀌는 경우에는 0의 카운트 + 1을 수행하고 (1을 0으로 바꿔야 하는 수 세기)
### 1에서 0으로 바뀌는 경우에는 1의 카운트 + 1을 수행한다. (0을 1로 바꿔야 하는 수 세기)
### 시작 숫자가 0인 경우 1로 빠꿔야 하므로 1의 count + 1 (1에서 0으로 넘어오는 것과 동일)
### 시작 숫자가 1인 경우 0으로 바꿔야 하므로 1의 count + 1 (0에서 1로 넘어오는 것과 동일 )

input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    
    oneCount = zeroCount = 0

    if string[0] == '0':
        oneCount += 1
    else :
        zeroCount += 1
    
    for currentIndex in range(1, len(string)) : 
        if string[currentIndex] != string[currentIndex - 1] : 
            if string[currentIndex] == '0' :
                oneCount += 1
            else :
                zeroCount += 1

    return min(oneCount, zeroCount)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)