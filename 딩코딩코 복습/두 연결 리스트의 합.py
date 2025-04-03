class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)



def get_linked_list_sum(linked_list_1, linked_list_2):
    # 연결리스트를 순회하면서 sum애 현재 데이터의 값을 더한다.단, sum을 * 10 한 뒤에 더하면 된다. 
    sumA = 0 
    
    curr = linked_list_1.head
    while curr is not None :
        sumA = sumA * 10 + curr.data
        curr = curr.next


    sumB = 0 
    
    curr = linked_list_2.head
    while curr is not None :
        sumB = sumB * 10 + curr.data
        curr = curr.next

    return sumA + sumB


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))