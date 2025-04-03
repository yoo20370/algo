# MX = 100005
# data = [-1] * MX 
# pre = [-1] * MX
# next = [-1] * MX 

# unused = 1

# def traverse(linkedList) -> None :
#     curr = 0

#     while next[curr] != -1 :
#         # 다음 포인터가 가리키는 값이 존재한다면 이동한 후 출력 
#         # 없으면 반복문 종료 
#         curr = next[curr]
#         print(data[curr], end = ' -> ')

#     print("None")

# def insert(addr, num) -> None :

#     # 다음 포인터 보존 
#     nextP = next[addr] 

#     next[addr] = unused

#     pre[unused] = addr

#     data[unused] = num

#     # 다음이 있었다면 
#     if nextP != -1 :
#         pre[nextP] = unused

#         nextP[unused] = nextP

#     unused += 1


# def erase(addr) :
#     # 다음이 있는 경우, 없는 경우에 대해서 처리해줘야 함 

#     if next[addr] != -1 :
#         nextP = next[addr]
#         preP = pre[addr]
#         next[preP] = nextP
#         pre[nextP] = preP
#     else :
#         preP = pre[addr]
#         next[preP] = -1

#     data[addr] = -1
#     pre[addr] = -1
#     next[addr] = -1

    
MX = 10000001

data = [-1] * MX
pre = [-1] * MX
next = [-1] * MX

unused = 1

def traverse() -> None :
    # 다음 노드가 존재한다면, 다음 노드로 이동한 다음 출력해준다.
    curr = 0
    while next[curr] != -1 : 
        curr = next[curr]
        print(data[curr], end = ' ')
    print()

def insert(addr, num) -> None :
    global unused

    if next[addr] != -1 :
        nextP = next[addr] 

        pre[nextP] = unused

        next[unused] = nextP 

    next[addr] = unused

    pre[unused] = addr

    data[unused] = num

    unused += 1
        

def erase(addr) :
    global unused

    if next[addr] != -1 :
        nextP = next[addr] 
        preP = pre[addr]

        next[preP] = nextP
        pre[nextP] = preP 
    else :
        preP = pre[addr]
        next[preP] = -1
    
    data[addr] = -1
    pre[addr] = -1
    next[addr] = -1


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


    

