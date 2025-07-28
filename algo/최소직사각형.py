# # 나는 이걸 어떻게 최소값을 구하나 ??
# # 60 50 
# # 70 50 
# # 70 50 
# # 80 50 

# # 둘 다 안 맞는 경우 -> 해당 형태로 만들어줘야 함 -> 60 50 
# # 둘 중 하나가 안 맞는 경우 -> 값을 올리는 것 중 더 작은 값을 올린다. 

# # 1차 풀이 실패 - bfs 전역 탐색 실패 (경우의 수 중복 계산 너무 많음)
# from collections import deque 

# def solution(sizes):
    
#     width, length = sizes[0]
    
#     if len(sizes) == 1 :
#         return width * length
    
#     min_size_sum = int(1e9)
    
#     queue = deque()
#     queue.append((width, length))
#     queue.append((length, width))
    
#     search_index = 1
#     while queue and search_index < len(sizes):
        
#         for _ in range(len(queue)) :
#             curr_width, curr_length = queue.popleft()
#             next_width, next_length = sizes[search_index]
            
#             if (curr_width >= next_width and curr_length >= next_length) or (curr_width >= next_length and curr_length >= next_width) :
#                 pass
#             else :
                
#                 if curr_width < next_width :
#                     curr_width = next_width
                
#                 if curr_length < next_length :
#                     curr_length = next_length
                
#             queue.append((curr_width, curr_length))
#             queue.append((curr_length, curr_width))
                
#         search_index += 1
        
#     while queue :
#         curr_width, curr_length = queue.popleft()
#         min_size_sum = min(min_size_sum, curr_width * curr_length)
        
#     return min_size_sum

# 우선 가장 큰 수가 하나 선택
# 다시 돌면서, 가로 세로 길이 중, 짧은 길이의 최대값을 구한다. 

def solution(sizes):
    answer = 0
    
    max_length = 0
    for row, col in sizes :
        max_length = max(max_length, row, col)
    
    max_size = 0
    for row, col in sizes :
        max_size = max(max_size, max_length * (min(row, col)))
    
    return max_size