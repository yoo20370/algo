shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):

    # prices와 coupons를 둘 다 오름차순 정렬한다.
    # prices와 coupons를 둘 다 pop() 하면 서 두 스택 중 하나가 동날 떄까지 수행한다.
    # 할인 적용이 안 되는 경우가 있을 수 있으므로 prices에 남은 값은 단순히 더해준다. 
    prices.sort()  # O(NlgN)
    coupons.sort() # O(NlgN) 

    total_cost = 0
    while prices and coupons : # O(N)
        price = prices.pop()
        coupon = coupons.pop()

        total_cost += price - (price * coupon // 100)

    total_cost += sum(prices)
    # 이 곳을 채워보세요!
    return total_cost


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))