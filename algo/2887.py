# 왕국은 N개의 행성으로 이루어져 있다.
# 행성을 연결하는 터널을 만드려고 한다.
## 두 행성을 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

import sys 

def cal_min_value(x1,y1,z1, x2,y2,z2) :
    return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    x_parent = find(parent, x)
    y_parent = find(parent, y)

    if x_parent < y_parent :
        parent[y_parent] = x_parent
    else :
        parent[x_parent] = y_parent

def solution() :
    plnet_count = int(sys.stdin.readline().rstrip())

    plnet_list = []
    for _ in range(plnet_count) :
        x, y, z = map(int, sys.stdin.readline().split())
        plnet_list.append((x,y,z))

    
   


solution()

## 어떻게 메모리를 아껴서 실행하지 ?? 지금 10만 *