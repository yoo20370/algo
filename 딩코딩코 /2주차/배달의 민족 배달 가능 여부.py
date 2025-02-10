shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

shop_menus.sort() # O(NlgN) + O(lgN)

# 항상 이진탐색을 사용하는 것은 비효율적

# def find_available_delivery_food(menus, order) :
    
#     result_list = []

#     for menu in order : 

#         pl = 0
#         pr = len(menus) - 1

#         while pl <= pr :
#             mid = (pl + pr) // 2

#             if menus[mid] < menu :
#                 pl = mid + 1
#             elif menus[mid] > menu :
#                 pr = mid - 1
#             else :
#                 result_list.append(menu)
#                 break
    
#     return result_list

def find_available_delivery_food(menus, order) :

    result_list = []

    menu_set = set(menus) 

    for menu in order :
        if menu in menu_set :
            result_list.append(menu)
    
    return result_list

result = find_available_delivery_food(shop_menus, shop_orders)
print(result)