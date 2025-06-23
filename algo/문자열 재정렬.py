import sys 

data = sys.stdin.readline().rstrip()

sum = 0 
string_list = []

for char in data :
    if char.isalpha() :
        string_list.append(char)
    else :
        sum += int(char)

string_list.sort()
print("".join(string_list) + str(sum))