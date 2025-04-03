def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    arr = [0] * 26


    for ch in string :
        if ch.isalpha() :
            curr = ord(ch) - ord('a')
            arr[curr] += 1

    maxVal = 0
    maxIdx = 0
    for currIdx in range(0, len(arr)) :
        if maxVal < arr[currIdx] :
            maxVal = arr[currIdx]
            maxIdx = currIdx
        
    return chr(maxIdx + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))