class Node :

    def __init__(self, value) :
        self.data = value
        self.next = None 

class LinkedList : 

    size = 0
    def __init__(self) :
        self.head = None 

    def append(self, value) -> bool :
        
        new_node = Node(value)

        if self.size == 0 :
            self.head = new_node
        
        else : 
            curr = self.head
            while curr.next != None : 
                curr = curr.next 
            
            curr.next = new_node
        
        self.size += 1
        return True
    
    def print_all(self) :

        curr = self.head

        while curr != None :
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def get_node(self, index) -> Node :


        curr = self.head
        curr_index = 0

        while curr != None :
            if curr_index == index :
                return curr
            curr_index += 1
            curr = curr.next 

        return False

    def add_node(self, index, value) -> bool :

        new_node = Node(value)

        if index == 0 :
            new_node.next = self.head
            self.head = new_node
            
        else : 
            prev_node = self.get_node(index - 1)
            if prev_node == None :
                return False
            next_node = prev_node.next
            new_node.next = next_node
            prev_node.next = new_node

        self.size += 1
        return True 

    def remove_node(self, index) -> bool :
        # 연결리스트가 비어있거나, 빈 공간을 제거하려 하는 경우 
        if self.size == 0 or self.size <= index :
            return False

        if index == 0 :
            self.head = self.head.next
        
        else :
            prev_node = self.get_node(index - 1)
            if prev_node == None :
                return False
            curr_node = prev_node.next 
            next_node = curr_node.next
            prev_node.next = next_node

        self.size -= 1
        return True


linkedList = LinkedList()

linkedList.append(0)
linkedList.append(1)
linkedList.append(2)
linkedList.append(4)
linkedList.append(5)
linkedList.append(6)

linkedList.add_node(3, 3)
linkedList.remove_node(0)
linkedList.print_all()

print(linkedList.get_node(5).data)
        

        
