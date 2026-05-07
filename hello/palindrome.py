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

def palindrome(string) :

    stringLength = len(string)

    totalStep = stringLength // 2

    pl = 0
    pr = stringLength - 1

    step = 0
    failCount = 0

    failStep = -1 
    while step < totalStep :

        if string[pl + step] != string[pr - step] :


            if failCount == 0 :
                failCount += 1
                failStep = step
                pl += 1
                continue

            elif failCount == 1 :
                failCount += 1
                step = failStep
                pl -= 1
                pr -= 1
                continue

            else : 
                return failCount
        
        step += 1

    if failCount == 0 :
        return failCount
    else :
        return 1
        

    
def solution() :
    
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T) :
        string = sys.stdin.readline().rstrip()

        print(palindrome(string))

solution()