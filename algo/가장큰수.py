# # numbers의 길이가 최대 100,000이므로 모든 가능한 수를 만들어서 정렬하는 방법은 안 됨 -> 100,000개를 조합해서 숫자를 만드는 것을 불가능 100,000! 개수 나옴
# # 그럼 어떤 방법을 ?? 
# # 같은 길이면, 큰 값이 앞으로 와야함 
# # 다른 길이면 ?? 9, 90 990, 998 -> 9 998 990 90이 가장 큰 값 (길이만 가지고 결정 불가)
# # 비교할 때, 더 큰 값을 만들 수 있는지 여부로 정렬해야 하나 ?? -> 90과 998이 있을 때, 90998과 99890을 만들어서 비교 -> 더 큰 값을 만드는 형태로 정렬 ?? 어려운뎅....
# ## 간단하게 생각하면, 두 숫자를 조합해서 더 큰 숫자가 앞으로 오면 될 듯, 그렇게 하나하나씩 맨 앞에 와야하는 숫자를 결정하고, 마지막에 이들을 이어 붙여서 만들면 될 듯 함 
# ## O(100,000 * 100,000) 시간복잡도 -> 불가능할 것 같은데 ㅠㅠ

# ### 1차 시도 불가 -> 너무 오래 걸림 100,000 * 100,000은 말도 안 되는 것이긴 함 
# def solution(numbers):
#     answer = ''
    
#     # 가장 큰 수부터 확정지어나갈 것임 -> 선택정렬을 사용하자 
#     # 선택 정렬로 간다. 
    
#     # i는 결정할 위치 
#     for i in range(0, len(numbers) - 1, 1) :
#         max_value_index = i
        
#         # j는 현재 최대값 인덱스 중 누가 더 큰 값인지 비교하기 위함 
#         for j in range(i + 1, len(numbers), 1) :
#             first = numbers[max_value_index]
#             second = numbers[j]
            
#             result1 = int(str(first) + str(second))
#             result2 = int(str(second) + str(first))
            
#             if result1 < result2 :
#                 max_value_index = j
#         numbers[i], numbers[max_value_index] = numbers[max_value_index], numbers[i]
    
    
#     for number in numbers :
#         if number != 0 :
#             answer += str(number)
    
#     return answer

## 숫자가 3자리이므로, 모든 수가 3자리 이상이 되도록 만든 후, 문자열 정렬하면 되는 문제
## 다만, 0만 들어오는 경우는 0을 반환해줘야 하므로 예외 처리해주면 됨 


def solution(numbers):
    str_numbers = sorted(map(str, numbers), reverse=True, key = lambda x : x*3)
    
    result = "".join(str_numbers)
    
    cnt = 0
    for number in str_numbers :
        if number == "0" :
            cnt += 1
            
    if cnt == len(str_numbers) :
        return "0"
    
    return result