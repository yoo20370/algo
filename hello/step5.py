
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    totalPrice = 0

    priceIndex = couponIndex = 0 

    while priceIndex < len(prices) and couponIndex < len(coupons) :
        totalPrice += int( prices[priceIndex] * ( 100 - coupons[couponIndex]) / 100)
        priceIndex += 1
        couponIndex += 1

    for index in range(priceIndex, len(prices)) :
        totalPrice += prices[index]
    
    return totalPrice

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))