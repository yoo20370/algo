N = int(input())
scoreList = list(map(int, input().split()))

length = len(scoreList)

sum = 0
maxScore = max(scoreList)
for i in range(length) :
    scoreList[i] = scoreList[i]/maxScore*100
    sum += scoreList[i]

avg = sum / length
print(avg)

