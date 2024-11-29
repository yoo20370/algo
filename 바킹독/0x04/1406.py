import sys

MX = 1000005
dat = [-1] * MX
pre = [-1] * MX
nxt = [-1] * MX

## 새 주소 
unused = 1 
length = 0

def insert(addr, data) :

    global length
    global unused
    # 연결리스트에 데이터 추가 
    dat[unused] = data

    # 주소의 다음 노드 포인터 
    nxtP = nxt[addr]

    # 추가된 노드의 이전을 addr 포인터로 설정
    pre[unused] = addr

    # addr의 다음 포인터를 추가된 노드로
    nxt[addr] = unused
    if nxtP != -1 :
        # 중간에 추가되는 경우

        # 추가된 노드의 다음을 addr의 다음 노드 포인터로 설정 
        nxt[unused] = nxtP

        # addr의 다음 노드의 이전을 새로 추가된 노드 포인터로 설정 
        pre[nxtP] = unused
    else :
        # 마지막에 추가하는 경우 
        nxt[unused] = -1
   
    length += 1
    unused += 1

def erase(addr) :
    global length 

    preP = pre[addr]
    nxtP = nxt[addr] 

    if nxtP != - 1 :
        # 중간 제거인 경우 
        pre[nxtP] = preP
    nxt[preP] = nxtP 

def traverse() :
    curr = 0 
    while nxt[curr] != -1 :
        curr = nxt[curr]
        print(dat[curr],end="")
    print()


inputData = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline().rstrip())

cursor = 0 
for i in range(len(inputData)) :
    insert(cursor, inputData[i])
    cursor = nxt[cursor]

for i in range(N) :
    command = sys.stdin.readline().split()

    if command[0] == "L" :
        if pre[cursor] != -1 :
            cursor = pre[cursor]
    
    elif command[0] == "D" :
        if nxt[cursor] != -1 :
            cursor = nxt[cursor]

    elif command[0] == "B" :
        if pre[cursor] != -1 :
            erase(cursor)
            cursor = pre[cursor]

    elif command[0] == "P" :
        insert(cursor, command[1])
        cursor = nxt[cursor]
    
traverse() 

