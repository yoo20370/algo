def solution(string):
    
    answer = len(string)
    for length in range(1, len(string) // 2 + 1) :    
        
        split = [string[start_index: start_index + length] for start_index in range(0,len(string), length)]
        
        # start_index와 compare_index를 비교해서 같으면 count 값과 compare_index를 1 증가시킨다.
        # 만약 compare_index 값과 start_index와 같지 않으면 count값을 확인한다. 이때 count 값이 1이하인 경우 result에 추가 
        # str(count) + start_index를 합친 것을 result에 추가한다. 
        # 그리고 start_index를 compare_index로 바꾸고 다음 과정을 반복한다. 언제까지 ??
        # start_index가 마지막 인덱스인 경우 반복문을 탈출
        # 마지막 인덱스를 result에 추가해준다.
        # 그리고 min_length와 비교해서 가장 짧은 문자열을 갱신해준다.
        
        result = ""
        temp = ""
        start_index = 0 
        compare_index = 0
        count = 0 
        while start_index < len(split) :
        
            if compare_index < len(split) and split[start_index] == split[compare_index] :
                temp += split[compare_index]
                count += 1 
                compare_index += 1 
            else : 
                if count <= 1 :
                    result += temp 
                    
                else :
                    # 압축이므로 문자 길이 + 숫자 
                    result += str(count) + split[0]
                temp = ""
                
                start_index = compare_index
                count = 0
        
        answer = min(answer, len(result))
    return answer