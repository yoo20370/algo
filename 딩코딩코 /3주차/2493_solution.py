import sys 

def get_receiver_top_orders(heights) -> list :
    result_list = [0 for _ in range(len(heights))]

    while heights :
        height = heights.pop()
        for curr_index in range(len(heights) - 1, -1, -1) :
            if heights[curr_index] >= height :
                result_list[len(heights)] = curr_index + 1
                break

    return result_list


N = int(sys.stdin.readline().rstrip())

heights = list(map(int, sys.stdin.readline().split()))

for i in get_receiver_top_orders(heights) :
    print(i, end=" ")

