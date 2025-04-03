# 암호는 서로 다른 L개의 알파벳 소문자들로 구성됨
# 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다. 
# 암호를 이루는 알파벳이 증가하는 순서로 배열되었을 것이라고 추측됨 

import sys, itertools

password_length, alpha_cnt = map(int, sys.stdin.readline().split())

alpha_list = sys.stdin.readline().split()

vowels = ("a", "e", "i" ,"o", "u")


for curr in itertools.combinations(alpha_list, password_length) :
    
    count = 0 
    for ch in curr :
        if ch in vowels :
            count += 1
        
    
    if count >= 1 and password_length - count >= 2 :
        print("".join(curr))