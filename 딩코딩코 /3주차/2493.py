import sys

tower_count = int(sys.stdin.readline().rstrip())
tower_height_list = list(map(int, sys.stdin.readline().split()))

def send_signal_tower(tower_height_list, tower_count) -> list :
    
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

print(send_signal_tower(tower_height_list, tower_count))
