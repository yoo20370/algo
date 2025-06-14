# a = 123.456

# # print(round(123.456)) # 123

# # print(round(123.456, 1)) # 123.5

# # print(5**3) # 125

# array = [1,2,3,5]

# array.insert(3, 4)

# print(array)

# print(array.count(1))

# array.remove(4)
# print(array)

# # 특정 값의 원소 모두 제거하기

# a = [1, 2, 3, 4, 5, 6, 7]

# remove_set = {3, 5}

# result = [i for i in a if i not in remove_set]

# print(result)

import bisect

array = [1, 2, 3, 3, 3, 4]

print(bisect.bisect_left(array, 3)) # 2
print(bisect.bisect_right(array, 3)) # 5