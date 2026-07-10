# 국영수
# N명의 이름과 국어, 영어, 수학 점수가 있음, 학생의 성적 정렬
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 
# 4. 모든 점수가 같으면 이름이 사전순으로 증가하는 순서로 

import sys

def solution() :
    n = int(sys.stdin.readline().rstrip())

    studentList = []
    for _ in range(n) :
        name, korean, english, math = list(sys.stdin.readline().split())
        studentList.append((name, int(korean), int(english), int(math)))
        
    studentList.sort(reverse=False, key=lambda x : (-x[1], x[2], -x[3], x[0]))

    for student in studentList :
        print(student[0])


solution()