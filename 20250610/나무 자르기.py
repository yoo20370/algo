import sys

# 어떻게 구현할 것인가 ??
# 절단기의 높이를 기준으로 이진탐색을 진행, 이때 시작 점은 가장 긴 나무의 길이로 지정한다. 
# 가장 긴 나무의 길이를 기준으로 이진 탐색을 진행하면서, 원하는 나무 길이를 얻을 수 있으면서도, 절단기의 높이가 가장 높은 것을 선택한다.
# 절단기의 높이가 높아야 최대한 적게 나무를 자를 수 있음,
# 구한 나무의 길이와 필요한 나무의 길이를 계산하여, 더 많은 나무가 필요하면 높이를 낮추고, 덜 잘라도 되면 높이를 높이는 방향으로 나무를 구한다.

def cut_tree() :

    tree_count, required_tree_length = map(int, sys.stdin.readline().split())
    tree_length_list = list(map(int, sys.stdin.readline().split()))

    min_cutter_length = 0
    max_cutter_length = max(tree_length_list)
    
    best_cutter_length = 0
    while min_cutter_length <= max_cutter_length :
        curr_cutter_length = (min_cutter_length + max_cutter_length) // 2
    
        curr_bring_tree_length = 0
        for tree_length in tree_length_list :
            if tree_length > curr_cutter_length :
                curr_bring_tree_length += tree_length - curr_cutter_length
        
        if curr_bring_tree_length < required_tree_length :
            max_cutter_length = curr_cutter_length - 1
        else :
            min_cutter_length = curr_cutter_length + 1 
            best_cutter_length = curr_cutter_length

    return best_cutter_length
    
print(cut_tree())