import sys
# 각 인접한 좌석끼리 바꿀 수 있다. 이 때, 점화힉은 f(n-1) + f(n-2)
# 좌석 4개일 때 경우의 수에 단순히 좌석 하나 붙인 경우의 수 -> f(n-1)
# 좌석 5개일 때 마지막 두 좌석을 바꾼 것의 경우의 수 -> f(n-2)
# n개의 좌석일 떄 인접한 좌석을 바꿀 수 있는 경우의 수 -> f(n-1) + f(n-2)

# 인접한 좌석의 개수는 vip_list를 만든 뒤, vip_list를 만나면 연속 좌석 리스트에 넣는다. 이 때, cnt가 0이라면 vip 좌석이 인접해있는 것으로 조심해야 함
# dp_table[0]을 = 1로 처리해줌으로써, 이를 vip 좌석이 연속적으로 배치되어도 문제가 없도록 함 

length = int(sys.stdin.readline().rstrip())
vip_cnt = int(sys.stdin.readline().rstrip())

vip_list = set()
for _ in range(vip_cnt) :
    vip_list.add(int(sys.stdin.readline().rstrip()))

dp_table = [1] * (length + 1) 
dp_table[2] = 2

for index in range(3, length + 1) :
    dp_table[index] = dp_table[index-1] + dp_table[index-2]

total_cnt = 1

cnt = 0 
for seat_number in range(1, length + 1) :
    if seat_number not in vip_list :
        cnt += 1
    else :
        if cnt != 0 :
            total_cnt *= cnt
        cnt = 0

total_cnt *= cnt
print(total_cnt)