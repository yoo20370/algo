import sys

tower_count = int(sys.stdin.readline().rstrip())
tower_height_list = list(map(int, sys.stdin.readline().split()))

def send_signal_tower(tower_height_list, tower_count) -> list :

    # 컴퓨터가 이 문제를 어떻게 해결할 수 있을까 생각

    # send_signal_tower_list가 비어 있다면, tower_height_list 맨 위의 타워의 인덱스와 높이 정보를 send_singal_tower에 삽입한다. 
    # 비어 있지 않다면, 인덱스 정보와 높이 정보를 꺼내어 비교한다.
    # 1. send_signal_tower 맨 위의 높이 정보와 비교한다.
    # 2. 만약 높이 정보가 더 높다면 send_signal_tower_stack의 맨 위 데이터를 pop하고, result_list에 정보를 기록한다. 
    #    -> send_signal_tower_stack에서 꺼낸 인덱스에 tower_height_list에서 pop한 데이터의 index + 1 값을 저장 후 
    # 3. tower_height_list에서 꺼낸 정보를 다시 tower_height_list에 저장한다. (send_signal_tower에 이전에 저장된 타워랑도 비교하기 위함)

    # 높이 정보가 더 낮다면 꺼낸 정보를 send_signal_tower_stack에 저장한다.

    # 결과를 반환한다. // 0으로 초기화했기 떄문에 tower_height_list가 비어 있다면 반복문을 종료 후 리스트 반환 
    
    result_list = [0 for _ in range(tower_count)]

    send_signal_tower_stack = []
    
    while tower_height_list :
        receive_tower_index = len(tower_height_list) - 1
        receive_tower_height = tower_height_list.pop()

        if send_signal_tower_stack :
            send_tower_index, send_tower_height = send_signal_tower_stack[-1]

            if receive_tower_height >= send_tower_height :
                send_signal_tower_stack.pop()
                result_list[send_tower_index] = receive_tower_index + 1
                tower_height_list.append(receive_tower_height)
            else : 
                send_signal_tower_stack.append((receive_tower_index, receive_tower_height))
                
        else : 
            send_signal_tower_stack.append((receive_tower_index, receive_tower_height))
    
    return result_list

for i in send_signal_tower(tower_height_list, tower_count) :
    print(i, end=" ")


