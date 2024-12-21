import sys

def str_reverse(data) -> int:
    sumVal = sum(data)
    if sumVal == len(data) or sumVal == 0 :
        return 0 
    
    if sumVal == 1 or len(data) - sumVal == 1 :
        return 1 
    else :
        return min(sumVal, len(data) - sumVal)

data = list()
pre = ''
for ch in sys.stdin.readline().rstrip() :
    if pre != ch :
        data.append(int(ch))
    pre = ch

print(str_reverse(data))