import sys

inputData = sys.stdin.readline().rstrip()

stack = list()
cnt = 0
before = ''
for char in inputData :    

    if char == '(' :
        stack.append('(')
    elif char == ')' :
        stack.pop()
        if before == '(' :
            cnt += len(stack)
        elif before == ")" :
            cnt += 1
    before = char
        
print(cnt)

# inp = input()
# ans = 0
# stack = []

# for i in range(len(inp)): 
#   if inp[i] == ')' and inp[i-1] == '(' : 
#     continue
#   if inp[i] == '(' and inp[i+1] == ')' :
#     # 레이저임
#     ans += len(stack)
    
#   elif inp[i] == ')': 
#     stack.pop()
#     ans += 1
#   else: 
#     stack.append(inp[i])

# print(ans)