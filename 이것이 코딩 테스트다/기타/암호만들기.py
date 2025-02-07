import sys, itertools

password_length, alphabet_length = map(int, sys.stdin.readline().split())

password_chars = list(sys.stdin.readline().split())

vowels_list = ['a', 'e', 'i', 'o', 'u']

password_chars.sort()

password_list = []

# password_chars를 정렬한다. (combinations은 정렬된 순서로 조합을 생성) -> 알파벳 순서 
# 조합을 모두 구한다. 
# 각 조합의 각 문자를 순회하면서 모음 개수와 자음 개수를 카운트한다. 
# 모음 자음의 경우 결과 리스트에 넣을 때, 개수를 충족하는지 검사한다. 

for combination in itertools.combinations(password_chars, password_length) :
    combination = list(combination)

    consonants_count = 0
    vowels_count = 0

    for char_index in range(len(combination)) :

        # 모음 카운트
        if combination[char_index] in vowels_list :
            vowels_count += 1
        else : # 자음 카운트 
            consonants_count += 1

    if vowels_count >= 1 and consonants_count >= 2:
        # 순서를 지키고, 모음 1개, 자음 2개 이상인 경우 패스워드 후보에 추가             
        print(''.join(combination))

    






