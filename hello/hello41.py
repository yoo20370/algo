# 회문 검사 
# 인덱스를 length // 2 만큼 이동하면서 서로 다른 값이 있는지 확인하는 걸로 구현하면 될 것 같음
# 짝수 길이인 경우 모두 검사함 
# 홀수 길이인 경우 굳이 중앙값을 검사할 필요가 없음 -> 어떤 문자가와도 나머지가 동일하다면 회문임 

input = "abcba"

def is_palindrome(string):

    length = len(string)

    pl = 0 
    pr = len(string) - 1

    mid = length // 2 

    for point in range(0, mid): 
        if string[pl + point] != string[pr - point] :
            return False
    return True

print(is_palindrome(input))