import sys 

arr = [0] * 10

max_val = 0
max_idx = 0
for i in sys.stdin.readline().rstrip() :
    s = i
    arr[int(i)] += 1
    
    # 6 혹은 9인 경우 
    if i == '6' or i == '9' and arr[int(s)] >= max_val:
        max_idx = int(s)
        max_val = arr[int(i)]
    elif arr[int(s)] > max_val :
        max_idx = int(s)
        max_val = arr[int(i)]

if max_idx == 6 :
    if arr[9] == 0 :

    if max_val % 2 != 0 :
        max_val += 1
    
    



