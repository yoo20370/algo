# 팀 결성

import sys

def findTeam(team, x) :
    if team[x] != x :
        team[x] = findTeam(team, team[x])
    return team[x]

def unionTeam(team, first, second) :
    firstTeam = findTeam(team, first)
    secondTeam = findTeam(team, second)

    if firstTeam < secondTeam :
        team[secondTeam] = firstTeam
    else :
        team[firstTeam] = secondTeam

def sameTeam(team, first, second) :
    return findTeam(team, first) == findTeam(team, second) 
        
 
def solution() :

    studentCount, commandCount = map(int, sys.stdin.readline().split())

    team = [i for i in range(studentCount + 1)]

    for _ in range(commandCount) :
        command, first, second = map(int, sys.stdin.readline().split())

        # 합치기 
        if command == 0 : 
            unionTeam(team, first, second)
        # 같은 팀 여부 확인 
        elif command == 1 :
            if sameTeam(team, first, second) :
                print("YES")
            else :
                print("NO")

solution()