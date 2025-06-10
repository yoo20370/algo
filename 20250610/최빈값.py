def find_max_occurred_alphabet(string):
    # 각 알파벳 등장 횟수를 저장할 길이 26의 배열을 만들고 모두 0으로 초기화한다.
    # 문자열을 순회하면서 각 문자를 아스키코드 값으로 변환하고 ord('a') 값을 빼 인덱스를 구하고 해당 인덱스 저장소에 + 1을 수행한다.
    # 배열을 순회하여 가장 큰 값을 갖는 인덱스를 찾는다. 
    # 해당 인덱스 값에 + ord('a')을 수행한 뒤 chr()을 이용해서 문자로 변환하여 결과를 출력한다.

    # 전체 시간 복잡도 O(N-1)
    alpha_count_list = [0] * 26

    for ch in string : # O(N)
        if not ch.isalpha() :
            continue
        index = ord(ch) - ord('a')
        alpha_count_list[index] += 1

    max_index = 0
    for index in range(1, len(alpha_count_list)) : # O(N-1)
        if alpha_count_list[max_index] < alpha_count_list[index] :
            max_index = index
    
    result_alpha = chr(max_index + ord('a'))
    return result_alpha


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))