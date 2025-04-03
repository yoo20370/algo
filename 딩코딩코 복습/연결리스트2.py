MX = 10000001

data = [-1] * MX 
prev = [-1] * MX 
next = [-1] * MX 

unused = 1

def traverse() -> None :
    # 인덱스 0에서 시작하여 순차적으로 순회한다.
    # 만약 다음이 없는 경우, 순회를 종료한다.
    # 0은 더미 노드 

    index = 0
    while next[index] != -1 :
        index = next[index]
        print(data[index], end=" ")        
    print()


def insert(addr, num) -> None :
    # addr 뒤에 값이 있는 경우
    # addr 뒤에 값이 없는 경우 

    # addr의 노드는 추가될 노드를 next에 추가해야 한다.
    # 추가될 노드는 addr 노드를 pre에 추가 해야 한다. 

    # addr의 다음 노드의 값을 저장한다. 
    # addr의 다음 노드가 추가된 노드를 가리키게 한다.
    # 추가된 노드가 next로 다음 노드를 가리키게 해야 한다.
    global unused

    newNode = unused
    data[newNode] = num
    unused += 1

    if next[addr] != -1 :
        nextNode = next[addr]

        prev[nextNode] = newNode

        next[newNode] = nextNode
    
    next[addr] = newNode

    prev[newNode] = addr

     
def erase(addr) -> None :

    # addr 뒤에 노드가 있는 경우와 없는 경우를 나눠서 처리해야 한다.
    
    # 다음 노드가 있는 경우 
    # 이전 노드의 정보를 저장한다. 
    # 다음 노드의 정보를 저장한다. 
    # 이전 노드가 다음 노드를 next로 가리키게 한다.
    # 다음 노드가 이전 노드를 prev로 가리키게 한다. 
    # 삭제한 노드의 모든 값을 -1로 초기화한다. 

    if next[addr] != -1 :
        nextNode = next[addr]

        prevNode = prev[addr]

        next[prevNode] = nextNode

        prev[nextNode] = prevNode

    data[addr] = prev[addr] = next[addr] = -1


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
