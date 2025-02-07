class Node :
    def __init__ (self, data) -> None :
        self.data = data 
        self.next = None 

class LinkedList :

    size = 1

    def __init__(self, value) -> None :
        self.head = Node(value)

    def append(self, value) :
        curr = self.head
        while curr.next != None :
            curr = curr.next
        
        curr.next = Node(value)
        self.size += 1

    def print_all(self) -> None :
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index) -> Node :
        
        curr = self.head
        curr_index = 0
        while curr != None :
            if curr_index == index :
                return curr
            curr_index += 1
            curr = curr.next
     
        return None
    
    # 해당 인덱스 다음에 삽입 
    def add_node(self, index, value) -> bool :

        new_node = Node(value)

        if index == 0 :
            new_node.next = self.head
            self.head = new_node
            
        else : 
            pre_node = self.get_node(index - 1)
            if pre_node == None :
                return False
            next_node = pre_node.next
            new_node.next = next_node
            pre_node.next = new_node

        self.size += 1
        return True 
    
    def remove_node(self, index) -> bool :
        
        # 연결리스트가 비어있거나, 빈 공간을 제거하려 하는 경우 
        if self.size == 0 or self.size <= index :
            return False

        if index == 0 :
            self.head = self.head.next
        
        else :
            pre_node = self.get_node(index - 1)
            if pre_node == None :
                return False
            curr_node = pre_node.next 
            next_node = curr_node.next
            pre_node.next = next_node

        self.size -= 1
        return True
    
        


linkedList = LinkedList(5)
linkedList.append(12)
linkedList.append(8)
print(linkedList.add_node(0,99))
print(linkedList.remove_node(3))
linkedList.print_all()
