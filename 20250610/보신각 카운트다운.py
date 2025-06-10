def count_down(number):
    if number == 0 : # 문제 종료 
        print("새해 복 많이 받으세요. !!!!")
        return 
    print(number)          # 카운트 다운 !!
    count_down(number - 1) # 문제 축소

count_down(60)