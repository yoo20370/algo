class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, value) :
        # 삽입 
        # 현재 노드의 next가 None인 곳에 집어 넣으면 됨 
        # Node를 생산해야 함 

        currentNode = self.head

        while currentNode.next != None :
            currentNode = currentNode.next

        # None인 경우니까 여기에 값을 넣으면 됨 
        currentNode.next = Node(value)

    
    def printLinkedList(self) :

        # 하나 하나 순회해가며 출력하면 됨 
        # currentNode.next가 없다면 진행하지 않으면 됨 

        currentNode = self.head

        while currentNode.next != None :
            currentNode = currentNode.next
            print(currentNode.data, end = " ")
    

    def searchValue(self, target) :

        # target을 찾을 때까지 순회하면 됨 
        # target을 찾았다면 바로 중단하고, 몇 번째 인덱스에 있는지 알려주고 값을 반환하면 됨 

        # 헤드가 0
        currentIndex = 0
        currentNode = self.head

        while currentNode.next != None :
            currentNode = currentNode.next
            currentIndex += 1

            if currentNode.data == target :
                return currentIndex
            
        return -1
    
    def insertValue(self, index, value) :

        # 특정 인덱스에 target 값을 삽입한다.
        # 두 가지 경우가 있음 
        # 삽입되는 위치가 마지막 위치인 경우 -> 삽입만 하면 됨
        # 삽입되는 위치가 중간인 경우 -> 이전 노드와 새 노드를 연결하고, 새 노드를 다음 노드와 연결해야 함 
        # 만약 인덱스 범위를 넘어선다면 ?? 

        # 일단 해당 인덱스까지 이동해야 함 
        # 이동하지 못한 경우 즉, 이전에 next == None인 경우 실패 처리 

        # head를 0으로 하겠다는 기준을 가지겠음 
        currentNode = self.head
        currentIndex = 0


        # 헤드에는 값을 넣지 못함 
        if index < 1 :
            print("적절하지 않은 인덱스 입니다.")
            return -1 
        
        # 삽입할 위치 -1 위치까지 이동할 거임 
        while currentNode.next != None :
            
            if currentIndex == index - 1 :
                break

            currentNode = currentNode.next
            currentIndex += 1

            

        if currentIndex != index - 1 :
            print("해당 인덱스가 존재하지 않습니다.")
            return -1 

        preNode = currentNode 

        nextNode = preNode.next 
        newNode = Node(value)

        preNode.next = newNode
        newNode.next = nextNode

        print("성공적으로 추가헀습니다.")        
        
    
    def remove(self, index) :

        currentNode = self.head
        currentIndex = 0 

        # 헤드에는 값을 넣지 못함 
        if index < 1 :
            print("적절하지 않은 인덱스 입니다.")
            return -1 
        
        # currentNode라는 단어는 이동할 때만 사용하는 단어 
        # 삽입할 위치 -1 위치까지 이동할 거임 
        while currentNode.next != None :
            
            if currentIndex == index - 1 :
                break

            currentNode = currentNode.next
            currentIndex += 1

        if currentIndex != index - 1 :
            print("해당 인덱스가 존재하지 않습니다.")
            return -1
        

        # 본격적으로 제거 작업 수행
        # 각 노드의 위치에 맞게 변수명 정의 
        preNode = currentNode
        removeNode = preNode.next
        nextNode = removeNode.next

        preNode.next = nextNode 

        print("정상적으로 제거되었습니다.")
        return removeNode.data

linked_list = LinkedList(5)
print(linked_list.head.data) # 5가 출력됩니다!

linked_list.append(4)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
linked_list.printLinkedList()

print()

result = linked_list.searchValue(3)
print(result)

linked_list.insertValue(1, 5)
linked_list.printLinkedList()
print()
linked_list.remove(1)
linked_list.printLinkedList()

# 현재 LinkedList 는 (5) 만 존재합니다!  