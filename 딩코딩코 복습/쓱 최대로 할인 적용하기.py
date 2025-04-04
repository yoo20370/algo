shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 가격에 대하여 오름차순 정렬 수행 -> O(NlogN)
# 할인율에 대하여 오름차순 정렬 수행 -> O(NlgN)
# 각각을 pop()한다. 이 때, 할인율 stack이 비어있지 않다면 꺼내서 할인된 가격을 적용한다.


def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()

    total_prices = 0
    # 할인 적용 
    while prices and coupons : 
        price = prices.pop()
        coupon = coupons.pop()

        total_prices += price - (price * coupon // 100)

    
    if prices :
        total_prices += sum(prices)

    return total_prices


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))