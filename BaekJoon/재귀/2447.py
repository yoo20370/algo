import sys 

def star10(data, idx) :

    N = len(data)
    # 종료조건 
    if N == 1 :
        return data
    
    l = N // 3
    r = l * 2
    
    mid = '*' * l
    
    # 특정 범위에 해당된다면 중앙을 
    if idx >= l and idx < r :
        mid = ' ' * l

    idx %= l

    # 문제 축소 
    left = star10(data[:l], idx)
    if mid != ' ' * l  :
        mid = star10(data[l:r], idx) 
    right = star10(data[r:], idx)
    
    return left + mid + right

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    print(star10("*"* N, i))

# 다른 사람 풀이 
# import sys
# input = sys.stdin.readline

# def draw_star(n):
#     """ 
#     크기 n의 별 패턴을 생성하는 재귀 함수
#     """
#     if n == 1:  
#         # 크기가 1인 패턴은 별 하나
#         return ["*"]
    
#     # N/3 크기의 패턴을 생성 (재귀적으로 호출)
#     sub_pattern = draw_star(n // 3)
#     pattern = []

#     # 첫 번째와 세 번째 줄: 작은 패턴 3개를 이어 붙임
#     for line in sub_pattern:
#         pattern.append(line * 3)

#     # 두 번째 줄: 가운데에 공백을 넣어 패턴 생성
#     for line in sub_pattern:
#         pattern.append(line + " " * (n // 3) + line)

#     # 첫 번째와 세 번째 줄과 동일
#     for line in sub_pattern:
#         pattern.append(line * 3)

#     return pattern

# # 입력 받기
# N = int(input())

# # 크기 N의 별 패턴 생성
# result = draw_star(N)

# # 결과 출력
# print("\n".join(result))

# # sys.stdout.write("\n".join(result) + "\n") 출력 성능이 더 중요한 경우(chat gpt)