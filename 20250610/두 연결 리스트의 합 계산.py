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

    def sum_linked_list(self) :
        sum = 0

        curr = self.head 
        while curr is not None :
            sum += curr.data
            curr = curr.next
        
        return sum 
    
    def linked_number(self) :
        result = 0
        curr = self.head
        while curr is not None :
            result = result * 10 + curr.data
            curr = curr.next
        return result


def get_linked_list_sum(linked_list_1, linked_list_2):
    return linked_list_1.linked_number() + linked_list_2.linked_number()


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))