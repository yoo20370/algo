import sys

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