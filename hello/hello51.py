shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    shop_prices_sorted = sorted(prices, reverse=True)
    user_coupons_sotred = sorted(coupons, reverse=True)

    priceIndex = couponIndex = 0

    totalCost = 0
    # 아직 둘 다 존재한다는 말 
    while priceIndex < len(shop_prices_sorted) and couponIndex < len(user_coupons_sotred) :


        totalCost += int(shop_prices_sorted[priceIndex] * (100 - user_coupons_sotred[couponIndex]) / 100)

        priceIndex += 1
        couponIndex += 1

    # 아직 계산 안 된 상품 추가 
    while priceIndex < len(shop_prices_sorted) :
        totalCost += shop_prices_sorted[priceIndex]
        priceIndex += 1

    return totalCost


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))