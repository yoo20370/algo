import sys

N = int(sys.stdin.readline().rstrip())

coins = [500, 100, 50, 10]
coin_idx = 0 

def moneyBack(remain_money) :
    coins = [500, 100, 50, 10]
    
    cnt = 0 

    for coin in coins :
        cnt += remain_money // coin
        remain_money = remain_money % coin

    print(cnt)

moneyBack(N)