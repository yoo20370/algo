## 거슬러줘야 하는 동전의 최소 개수 
## 돈은 항상 N은 10의 배수 
## 결국 가장 큰 값으로 처리가 가능한지 체크해야 함 


coins = [500, 100, 50, 10]
count = 0

currentMoney = int(input())

for coin in coins :
    coinCount = currentMoney // coin 
    count += coinCount

    currentMoney = currentMoney % coin


print(count)







