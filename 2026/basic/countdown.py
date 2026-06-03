# 종료 조건
# 축소 조건 

def count_down(number):
    if number == -1 :
        print("Happy NewYear")
        return 
    print(number)
    count_down(number - 1)
count_down(60)