finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array) -> bool :
    # 이 부분을 채워보세요!
    array.sort()

    pl = 0 
    pr = len(array) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if array[mid] < target :
            pl = mid + 1
        elif array[mid] > target :
            pr = mid - 1
        else :
            return True

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)