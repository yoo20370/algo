shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    # 주문에 있는 데이터를 menus에 있는지 확인하면 된다.
    # menus의 값을 set으로 변환하고, orders를 순회하면서 각각 존재하는지 in 연산자로 확인하면 될 것 같다.
    # set은 내부적으로 해시테이블을 사용하기 때문에 데이터가 적다면 해시충돌 위험이 줄어들어, set을 사용하는게 훨씬 좋다.
    
    result = []

    menus_set = set(menus)

    for menu in orders :
        result.append(True if menu in menus_set else False)
    return result

result = is_available_to_order(shop_menus, shop_orders)
print(result)   