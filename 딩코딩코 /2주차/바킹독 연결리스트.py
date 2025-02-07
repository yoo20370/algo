# 연결 리스트 파이썬으로 구현 
MX = 1000005
dat = [-1] * MX # 원소를 관리하는 배열 
pre = [-1] * MX # 이전 원소의 포인터 대신 이전 원소의 인덱스 저장 
nxt = [-1] * MX # 다음 원소의 포인터 대신 다음 원소의 인덱스 저장 
               # pre[idx] or nxt[idx]의 값이 -1이면 이전 또는 다음 원소가 존재하지 않는다는 의미
unused = 1     # 새로운 원소가 들어갈 수 있는 인덱스, 원소가 추가되면 1씩 증가한다.
               # 0 번지는 시작 원소로 고정되어 있다., 0번지는 값이 들어가지 않고 시작점을 나타내는 dummy node 
               # 길이가 필요하다면 len 변수를 두고 원소가 추가될 때 1증가시키고 제거될 때 1감소시키면 된다.

def traverse() :
    idx = 0
    while nxt[idx] != -1 :
        idx = nxt[idx]
        print(dat[idx], end=" ")
    print()


## addr이 2번지 2번지 뒤에 추가하고 싶으면 insert(2,20)
def insert(addr, num) :
    global unused

    if nxt[addr] != -1 :
        # 다음 원소 포인터 
        nxtp = nxt[addr]

        # 추가된 원소가 다음 원소를 가리킴 
        nxt[unused] = nxtp
        
        # 다음 원소가 추가된 원소를 가리킴 
        pre[nxtp] = unused

    # 추가된 원소가 이전 원소를 가리킴 
    pre[unused] = addr

    # addr의 원소가 추가된 원소를 가리킴 
    nxt[addr] = unused        
    
    # 데이터 추가 
    dat[unused] = num

    # 추가된 원소의 다음 주소 설정 
    unused += 1

def erase(addr) :
    # 다음 원소가 있을 때 
    if nxt[addr] != -1 :
        # 다음 원소 포인터
        nxtP = nxt[addr]
        # 이전 원소 포인터
        preP = pre[addr]

        # 이전 원소도 다음 원소를 가리켜야 함 
        nxt[preP] = nxtP

        # 다음 원소가 이전 원소를 가리켜야 함 
        pre[nxtP] = preP
        
    else :
        # 이전 원소 포인터 
        preP = pre[addr]

        # 이전의 다음 포인터가 null을 가리켜야 함
        nxt[preP] = -1

    # 삭제된 원소 메모리 초기화    
    dat[addr] = -1
    pre[addr] = -1
    nxt[addr] = -1

insert(0, 10)
traverse()
insert(0, 30)
traverse()
insert(2, 40)
traverse()
insert(1, 20)
traverse()
insert(4, 70)
traverse()

print()
print()

erase(1)
traverse()
erase(2)
traverse()
erase(4)
traverse()
erase(5)
traverse()