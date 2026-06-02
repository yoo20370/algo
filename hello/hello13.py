import sys 

def solution() :

    N, M = map(int, sys.stdin.readline().split())

    # 왜 있어야 함 -> 아이스 틀이 어떻게 되어있는지 알아야 하기 때문에 모두 저장해서 가지고 있어야 함
    # 왜 배열 ? 2차원 배열로 아이스틀을 표현하는게 적절하다고 생각했음
    iceFrame = []

    for _ in range(N) :
        iceFrame.append(list(sys.stdin.readline().rstrip()))

    # 동, 서, 남, 북
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]    

    # dfs로 처리할 예정 

    # 0이면 비어 있음, 1이면 칸막이 
    # 0이면 카운트하고 -1로 방문했다고 표시하면 됨, 왜 1로 안 함 ?? -> 칸막이랑 이미 방문한 것을 구분할 필요도 있어보임, 여기서는 필요 없지만 구현상 
    # 그러면 모든 얼음칸을 확인해서 0인 곳을 찾은 후, 그 0인 위치에서 dfs를 통해 모두 방문처리한다. 

    count = 0

    for row in range(N) :
        for col in range(M) :
            if iceFrame[row][col] == '0' :
                count += 1 
                # 깊이 우선 탐색을 통해 방문할 필요가 없는 칸을 처리해주자 
                stack = [(row,col)]

                while stack :
                    currentRow, currentCol = stack.pop()

                    # 아직 방문하지 않은 칸이 중복해서 stack에 삽입되는데, 이 조건이 없으면 불필요한 반복문 호출 됨 
                    if iceFrame[currentRow][currentCol] == '-1' :
                        continue

                    # 방문 처리 
                    iceFrame[currentRow][currentCol] = '-1'

                    # 인접한 4개의 칸에 대하여 접근
                    for distance in range(len(direction)) :
                        moveRow, moveCol = direction[distance]

                        nextRow = currentRow + moveRow
                        nextCol = currentCol + moveCol

                        # 그래프 범위 내의 인덱스고 아직 방문하지 않았다면 스택에 삽입  
                        if nextRow >= 0 and nextRow < N and nextCol >= 0 and nextCol < M and iceFrame[nextRow][nextCol] == '0' :
                            stack.append((nextRow, nextCol))

    print(count)

solution()