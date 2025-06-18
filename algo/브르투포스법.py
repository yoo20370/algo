import sys

def bf() :
    text, pattern = sys.stdin.readline().split()

    # text 길이 - pattern 길이 만큼 외부 반복문이 돌아야한다. 
    # 내부 반복문에서는 pattern과 일치하는 문자열이 있는지 확인한다. 
    # 만약 내부 반복문 수행 중 틀린 것이 있다면 continue한다. 
    # 만약 끝까지 잘 수행한다면 count를 증가시킨다.

    count = 0
    text_length = len(text)
    pattern_length = len(pattern)

    pt = 0
    pp = 0 

    while pt != text_length and pp != pattern_length :

        if text[pt] == pattern[pp] :
            pt += 1
            pp += 1
        else :
            pt - pp + 1 
            pp = 0

    return pt - pp + 1 if pp == len(pattern) else -1 


print(bf())

