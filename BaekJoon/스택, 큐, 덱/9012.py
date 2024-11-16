import sys

N = int(sys.stdin.readline().rstrip())

def check(s) :
    stack = list()
    for i in s :
        if i == '(' :
            stack.append('(')
        elif len(stack) != 0 and i == ')' :
            stack.pop()
        else :
            return "NO"
    
    if len(stack) == 0 :
        return "YES"
    else :
        return "NO"


for i in range(N) :
    data = sys.stdin.readline().rstrip()
    print(check(data))
    

## 스택을 사용하지 않고 풀 수 있음 
# def isVPS(targ):
#     q = 0
#     for cur in targ:
#         if cur == '(':
#             q += 1
#         elif (cur == ')' and q > 0):
#             q -= 1
#         else:
#             return 'NO'
#     if q > 0:
#         return 'NO'
#     return 'YES'
    
    
# T = int(input())
# res = []
# for _ in range(T):
#     res.append(isVPS(input()))
    
# for i in res:
#     print(i)
    