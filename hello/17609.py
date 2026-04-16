# # 대칭인 경우 회문 -> 0 출력
# # 유사 회문 -> 한 문자를 삭제하여 회문이라면 -> 1 출력
# # 그 외는 2출력

# # 슬라이스로 접근하면 시간 복잡도가 너무 높음 
# # 인덱스로 접근해야 할 것 같음 -> 재귀든 모든 
# # 유사 회문은 어떻게 할거야 ??
# # 왼쪽을 제거해보고 재귀 -> 문제 없으면 유사 회문 -> 1
# # 왼쪽 제거해도 문제 -> 오른쪽 제거 -> 문제 없으면 유사 회문 -> 1
# # 둘 다 제거 해봤는데 문제 있음 -> 2 출력 
# # 왜 문제 있을 때 검사하나요 ? -> 거기서 회문이 안 된 거니까 그 주변을 제거해봐야죠 

# import sys

# sys.setrecursionlimit(int(1e5))

# def palindrome(string, leftIndex, rightIndex, count) :

#     # 종료 조건 - 같거나 교차한 경우 
#     if leftIndex >= rightIndex :
#         return count
    
#     # 문제가 없는 경우 다음 단계로 전진
#     if string[leftIndex] == string[rightIndex] :
#         return palindrome(string, leftIndex + 1, rightIndex -1, count)
    
#     # 문제가 생겼으므로 왼쪽 제거 or 오른쪽 제거하여 진행 
#     if count == 0 :

#         # 문제가 있을 수도 있고, 없을 수도 있음 
#         result = palindrome(string, leftIndex + 1, rightIndex, count + 1)

#         # 문제가 있다면, 오른쪽 제거하고 진행
#         if result == 2 :
#             return palindrome(string, leftIndex, rightIndex - 1, count + 1)
        
#         return result

#     else :
#         return 2


# def solution() :
    
#     loop = int(sys.stdin.readline().rstrip())

#     for _ in range(loop) :
#         string = sys.stdin.readline().rstrip()
    
#         result = palindrome(string, 0, len(string) - 1, 0)
#         print(result)        

# solution()

