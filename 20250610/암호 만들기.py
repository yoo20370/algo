# 서로 다른 L개의 알파벳 소문자들로 구성됨 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다고 함 
# 알파벳이 증가하는 순서로 배열됨 
# C 가지 알파벳이 주어졌을 떄, 가능성 있는 모든 암호들을 구하는 프로그램 

# 어떻게 풀 것인가 ??
# 우선 입력으로 들어온 알파벳 목록을 정렬 수행  
# 모음은 set에 저장해준다. 
# 모음의 개수를 체크한다.
# 길이 - 모음이 2개 이하면 제외 
import sys
from itertools import combinations

password_length, alpha_count = map(int, sys.stdin.readline().split())
alpha_list = sys.stdin.readline().split()

# 모음
vowels = ("a","e","i","o","u")

alpha_list.sort()

result_list = []
for password in combinations(alpha_list, password_length) :
    count = 0
    for char in password :
        if char in vowels :
            count += 1
    
    if count >= 1 and password_length - count >= 2 :
        print("".join(password))

    