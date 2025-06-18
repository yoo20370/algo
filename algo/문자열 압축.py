# 어떻게 풀래 ??

# aabbaccc -> 1글자 연속되는거 확인하면 됨 

# 2a 2b a 3c 
# -> 즉, 글자 길이 1개씩 증가하면서 비교하면 되지 않을까 ??

# 가능한 모든 패턴을 찾는다.
# 그리고 글자 1개부터 글자 len(text) // 2 까지 순회하면서 체크한다.
# 만약 패턴이 a, b, c가 있다고 한다면
# a를 마주했을 때 패턴 리스트에 해당하는 패턴이 있는지 찾는다. 찾았다면 패턴 길이 만큼 이동하여 cnt를 구한다.
# 패턴과 다른 문자를 찾았다면 해당 cnt가 1이 아닐 때, 압축을 진행해서 결과 리스트에 넣는다.
# 그리고 다시 패턴 리스트를 처음부터 순회하여 해당하는 패턴이 있는지 찾는다. (해당하는 패턴이 없다면 오류)
# 이런 식으로 패턴 길이별 최대 압축 길이를 구해서 그 중 최소 값을 반환하도록ㅎ ㅏㄴ다.

# 우선 패턴부터 저장해야할 것 같다. 
# pattern_list에 패턴을 2차원 배열로 저장할 예정 
# 

# 2 + 1 3

# 1 -> len(s) 
# 2 -> len(s) - 1
# len(s) -> 6 - 2 -> 4
# 0 1 2 3 4 
# length -> 5 
# 5 // 2 + 1 -> 3 
# pattern -> 0, 1, 2 

def solution(s):
    # 1일 때 반례를 찾지 못해서 혼자 풀지 못함 -> 왜 1일 때 걸러주지 못했는지 확인해보자 
    if len(s) == 1 :
        return 1
    
    # 1인 경우는 패턴도 못 만든다. 1 // 2 + 1 = 1이므로 [[]] 형태로 이차원 테이블 생성 
    # 패턴 리스트 부터 만들어보자 
    # 패턴 리스트의 경우 문자열 절반보다 길 필요가 없음 -> 길면 반복 불가 
    pattern = [[] for _ in range(len(s) // 2 + 1)]
    
    # 길이 
    for length in range(1, len(s) // 2 + 1) :
    
        start_index = 0
        while start_index <= len(s) - length :
            pattern[length].append(s[start_index: start_index + length])
            start_index += length
    
    length_list = []
    
    # 이제 할 거임 
    # 1부터 len(s) // 2 길이까지 진행 
    for length in range(1, len(s) // 2 + 1) :
        
        result = ""
        start_index = 0 
        while start_index <= len(s) - length :
            
            # 비교할 텍스트  
            curr_str = s[start_index:start_index + length] 
            
            # 비교할 패턴 찾기 
            for pattern_str in pattern[length] :
                
                # 비교할 텍스트와 패턴이 같은 경우 
                if curr_str == pattern_str :
                    
                    init_index = start_index
                    # 몇 번 연속적으로 나타나는지 
                    cnt = 0 
                    while curr_str == pattern_str :
                        cnt += 1
                        start_index += length 
                        curr_str = s[start_index:start_index + length]
                        
                    if cnt <= 1 :
                        result += s[init_index:start_index]
                    else : 
                        result += str(cnt) + pattern_str
    
        if start_index < len(s) :                        
            result += s[start_index:]
        length_list.append(len(result))
    
    return min(length_list)