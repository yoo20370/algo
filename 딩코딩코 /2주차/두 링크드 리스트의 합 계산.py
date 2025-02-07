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

# def traversal(linkedList) -> str :
#     # 순회하면서 하나 하나 data를 꺼낸다. 그래서 문자열로 합한다.
#     # 두 개의 링크드 리스트가 있기 때문에 두 개의 for문을 사용한다. -> 둘 다 길이가 다를 수 있기 때문 

#     string = ""
#     curr = linkedList.head

#     while curr != None :
#         string += str(curr.data)
#         curr = curr.next 

#     return string

def traversal(linkedList) -> int :

    sum = 0 
    curr = linkedList.head
    while curr != None :
        sum = sum * 10 + curr.data 
        curr = curr.next

    return sum

def get_linked_list_sum(linked_list_1, linked_list_2):

    num1 = traversal(linked_list_1)
    num2 = traversal(linked_list_2)

    return num1 + num2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
