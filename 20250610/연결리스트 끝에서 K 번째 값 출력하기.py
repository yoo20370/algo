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

    def get_kth_node_from_last(self, k):
        # 어떻게 풀까 ?? 
        # 투 포인터를 두고 순회하다가 특정 범위까지 curr가 이동하면, 2번째 포인터도 함께 이동하도록 구현해볼까 ??
        # 먼저 k만큼 첫 번째 포인터를 이동시키고, 그 다음부터는 같이 움직인다.
        one_point = self.head
        two_point = self.head
        
        for _ in range(k) :
            one_point = one_point.next
            
        while one_point is not None :
            two_point = two_point.next
            one_point = one_point.next
            

        return two_point

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)


print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!