finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
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

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)