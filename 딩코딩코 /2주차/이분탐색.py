array = [0, 3, 5, 6, 1, 2, 4]

def binary_search(array, target) :

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

array.sort()
print(binary_search(array, 2))