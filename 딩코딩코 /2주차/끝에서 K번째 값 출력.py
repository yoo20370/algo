class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 첫 번째 성능 개선 
# 두 개의 포인터를 사용하면 성능 개선 가능
# fast, slow 노드를 둔다. 항상 K만큼 떨어져 있게 한다.

# 두 번째 성능 개선 
# 

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k): 
        
        slow_index = -k
        fast_index = 0 
        slow = self.head
        fast = self.head

        while fast != None :
            if slow_index >= 0 :
                slow = slow.next 
            
            fast = fast.next

            fast_index += 1
            slow_index += 1
        
        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!