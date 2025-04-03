def summarize_string(input_str):
    # 26개짜리 배열을 선언하고 0으로 모두 초기화한다.
    # 문자열을 순회하면서 배열에 개수를 업데이트한다.
    # 배열을 순회하면서 0이 아닌 데이터에 대하여 문자열을 만들어서 반환한다.

    alpha = [0] * 26

    for ch in input_str :
        chageNum = ord(ch) - ord('a')
        alpha[chageNum] += 1


    resultStr = ""
    for idx in range(len(alpha)) :
        if alpha[idx] != 0 :
            if resultStr != "" : resultStr += "/"
            resultStr += chr(idx + ord('a')) + str(alpha[idx])

    return resultStr
    

input_str = "acccdeee"

print(summarize_string(input_str))