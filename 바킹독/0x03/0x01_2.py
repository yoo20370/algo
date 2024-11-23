
# def func2(arr, length) :
#     temp = [0] * 101
#     for i in arr :
#         temp[i] += 1

#     for i in arr :
#         idx = 100 - i 
#         if temp[idx] != 0 and idx != 50 :
#             return 1
#         if idx == 50 and temp[idx] > 1:
#             return 1
#     return 0
        
# print(func2([1,52,48],3))
# print(func2([50,42],2))
# print(func2([4,13,63, 87],4))

def func2(arr, length) :
    temp = [0] * 101

    for i in range(length) :
        if temp[100-arr[i]] == 1 :
            return 1
        temp[arr[i]] += 1
        
    return 0
        
print(func2([1,52,48],3))
print(func2([50,42],2))
print(func2([4,13,63, 87],4))