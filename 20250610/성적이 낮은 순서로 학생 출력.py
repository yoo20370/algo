import sys

stu_count = int(sys.stdin.readline().rstrip())

student_array = []
for _ in range(stu_count) :
    student_info = sys.stdin.readline().split()
    student_array.append((student_info[0], int(student_info[1])))

student_info.sort(key= lambda x : x[1])

for name, score in student_array :
    print(name, end=" ")