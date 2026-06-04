# 최빈값을 찾아라 
# 문자열의 등장횟수를 기록할 a ~ z 배열을 생성 (a = 0) -> O(1)
# 문자열을 순회하면서 몇 번 등장했는지 배열에 기록 O(N)
# 가장 높은 값이 무엇인지 확인 -> O(N)



def find_max_occurred_alphabet(string):

    alpha = [0] * 26

    # 몇 번 등장했는지 확인 
    for char in string :
        
        if char.isalpha() :
            charIndex = ord(char) - ord('a')
            alpha[charIndex] += 1 

    maxValueIndex = 0
    for currentIndex in range(1, len(alpha)) :
        if alpha[maxValueIndex] < alpha[currentIndex] : 
            maxValueIndex = currentIndex

    maxValue = alpha[maxValueIndex] 
    count = 0 
    for value in alpha :
        if maxValue == value :
            count += 1

    # 최빈값이 두 개 이상인 경우
    if count > 1 :
        return -1 
    else :
        chr(maxValueIndex + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))