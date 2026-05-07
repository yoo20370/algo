shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def searchMenu(orderMenu, menus) :
    pl = 0 
    pr = len(menus) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if menus[mid] < orderMenu :
            pl = mid + 1
        elif menus[mid] > orderMenu :
            pr = mid - 1
        
        else :
            return True
    
    return False

def is_available_to_order(menus, orders):
    
    

    for menu in orders :

        result = searchMenu(menu, menus)

        if not result :
            return False

    return True

shop_menus.sort()
result = is_available_to_order(shop_menus, shop_orders)
print(result)