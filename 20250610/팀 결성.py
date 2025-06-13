import sys 

sys.setrecursionlimit(int(1e9))
def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(x, y, parent) :
    parent_x = find(parent, x)
    parent_y = find(parent, y)

    if parent_x < parent_y :
        parent[parent_y] = parent_x
    else :
        parent[parent_x] = parent_y

def check_same_team(teamA, teamB, team_table) :
    if find(team_table, teamA) == find(team_table, teamB) :
        return True
    return False

def team_union() :

    team_count, command_count = map(int, sys.stdin.readline().split())

    team_table = [i for i in range(team_count + 1)]
    for _ in range(command_count) :
        command, teamA, teamB = map(int, sys.stdin.readline().split())

        if command == 0 : 
            union(teamA, teamB, team_table) 

        elif command == 1 :
            if check_same_team(teamA, teamB, team_table) :
                print("YES")
            else :
                print("NO")

team_union()