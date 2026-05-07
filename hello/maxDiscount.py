shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    priceIndex = 0
    couponIndex = 0

    totalCost = 0
    while priceIndex < len(prices) and couponIndex < len(coupons) :
        totalCost += int(prices[priceIndex] *(100 - coupons[couponIndex]) // 100)
        priceIndex += 1
        couponIndex += 1

    for index in range(priceIndex, len(prices), 1) :
        totalCost += prices[index]

    return totalCost


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))