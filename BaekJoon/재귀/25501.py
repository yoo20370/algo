import sys 

def pal(data, l_idx, r_idx, cnt) :
    cnt += 1
    if l_idx >= r_idx :

        return 1, cnt
    elif data[l_idx] != data[r_idx] :
        return 0, cnt 
    else :
        return pal(data, l_idx +1, r_idx -1, cnt)

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    data = sys.stdin.readline().rstrip()
    x, y = pal(data, 0, len(data)-1, 0)
    print(x, y)