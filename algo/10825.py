import sys 

def solution() :
    N = int(sys.stdin.readline().rstrip())

    # 국, 영, 수
    score_list = []
    for _ in range(N) :
        name, kor, eng, math = sys.stdin.readline().split()
        score_list.append((name, int(kor), int(eng), int(math)))


    score_list.sort(key=lambda x : (-x[1], x[2], -x[3], x[0])) 

    for name, a, b, c in score_list :
        print(name)

solution()