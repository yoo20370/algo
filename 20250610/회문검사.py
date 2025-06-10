input = "abcacba"

def is_palindrome(string):
    # 어떻게 구현할 것인가 ?? 
    # 배열의 처음과 끝을 비교한다. array[0] - array[-1] 비교 
    # 그리고 재귀를 통해서 특정 배열 길이 만큼 입력값으로 전달 (축소 조건) strint[1:-1]
    # 문자열의 길이가 1보다 작다면 종료 조건 -> 3개인 경우 1개만 남고, 2개인 경우 0개가 남기 때문
    if len(string) <= 1 :
        return True
    
    if string[0] != string[-1] :
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))