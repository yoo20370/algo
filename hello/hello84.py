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