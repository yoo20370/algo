import sys


# 앞 뒤 방향으로 봤을 때 동일하면, 회문 0 
# 한 글자만 뺏을 때 동일하면 유사 회문 1
# 나머지는 회문 아님 2 

# 솔직히, 재귀로 풀어야겠다는 생각했는데, 반복문으로 풀어보고 싶음 
# 일단 한 번 해보자 
# 일단 length // 2 만큼, 이동해서 체크해야 함
# 이때, pl과 pr을 둬야 함, 그리고 pl과 pr을 비교했을 때, 모두 같으면 회문
# 다르면 pl + 1 혹은 pr -1을 한 뒤 다시 실행하여 진행 
# 이때 문제 없으면 유사 회문
# 둘 다 문제 있으면 그냥 실패 
def palindrome(string) :

    checkLength = len(string) // 2

    pl = 0
    pr = len(string) - 1


    
def solution() :
    
    T = int(sys.stdin.readline().split())

    for _ in range(T) :
        string = sys.stdin.readline().split()

        print(palindrome(string))

solution()