import sys

# 앞 뒤 방향으로 봤을 때 동일하면, 회문 0 
# 한 글자만 뺏을 때 동일하면 유사 회문 1
# 나머지는 회문 아님 2 

# 반복문으로 풀려면 어떻게 해야 할까 ?? 
# 결국 정해진 회차를 수행했을 때 문제 없으면 회문
# 정해진 회차를 수행했을 때, 한 번만 문제가 있으면 유사 회문 
# 두 번 이상 문제가 있으면 그 외로 분리해야 함 

# 결국 문제가 있으면, pl + 1 or pr - 1과 비교하는 방향으로 진행해야 함
# 결국 왼쪽 틀린 것과 오른쪽 틀린 것을 구분해야 함 

# 틀렸어, 근데 왼쪽이랑 오른쪽이랑 구분해줘야 함 

def palindrome(string, left, right, removed) :

    if left >= right :
        if removed :
            return 1
        else :
            return 0
        
    
    if string[left] != string[right] :

        if removed :
            return 2
        
        leftCase = palindrome(string, left + 1, right, True)
        rightCase = palindrome(string, left, right - 1, True)

        if leftCase != 2 or rightCase != 2 :
            return 1
        
        return 2

    else :
        return palindrome(string, left + 1, right - 1, removed)

        
def solution() :
    
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T) :
        string = sys.stdin.readline().rstrip()

        print(palindrome(string, 0, len(string) - 1, False))

solution()