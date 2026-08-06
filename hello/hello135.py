# 결국 열쇠를 회전해서, 자물쇠의 홈에 끼워 넣을 수 있느냐를 판단해야 함 
# 결국 동, 서, 남, 북 회전해야 함 

# 전역탐색하는 방법
# 더 줄일 수 없으려나 ?? 
# 동, 서, 남, 북 회전하면서, 가능한 모든 경우를 set()에 저장
# Lock의 좌표에 Key 가능한 좌표를 차집합했을 때, Lock Set이 비어있으면 성공,
# 실패라면 False 하면 되지 않을까 ?? 

# Set에 저장하는 이유는 중복을 제거하기 위함 
# 모든 경우는 반드시 탐색해야 함

# 0 0 0
# 1 0 0 
# 0 1 1  

# 90도 회전 
# 0열은 0행이 됨 
# 1열은 1행이 됨
# 2열은 2행이 됨 

# (0,0) -> (0, 2)
# (1,0) -> (0, 1)
# (2,0) -> (0, 2)

# N이 인덱스이기 때문 
# 열 (N - 1) - row
# 행 col 

# (1, 1) -> (1, 1)

# 열 (3 - 1) - 1 = 1
# 행 col = 1

def solution(key, lock):
    
    keyEdgeLength = len(key[0])
    
    keyBumps = set()
    for row in range(keyEdgeLength) :
        for col in range(keyEdgeLength) :
            if key[row][col] == 1 :
                keyBumps.add((row, col))

    lockEdgeLength = len(lock[0])
                
    LockGrooves = set()
    LockBumps = set()
    for row in range(lockEdgeLength) :
        for col in range(lockEdgeLength) :
            if lock[row][col] == 0 :
                LockGrooves.add((row, col))
            else :
                LockBumps.add((row, col))                
    
    
    
    # 시작 위치 인덱스임 
    startRow = startCol = -keyEdgeLength + 1
    endRow = endCol = lockEdgeLength + keyEdgeLength - 1
    
    # 4방면 모두 검사하겠다. 
    for _ in range(4) :
        keyBumps = rotation90(keyBumps, keyEdgeLength)
        
        for currentRow in range(startRow, endRow) :
            for currentCol in range(startCol, endCol) :
                
                currentkeyBumps = set()
                for keyBump in keyBumps:
                    moveRow, moveCol = keyBump
                    
                    nextBumpRow = currentRow + moveRow
                    nextBumpCol = currentCol + moveCol
                    
                    currentkeyBumps.add((nextBumpRow, nextBumpCol))
                
                result1 = LockBumps - currentkeyBumps
                result2 = LockGrooves - currentkeyBumps
                

                if result1 == LockBumps and not result2 :
                    return True
    
    return False

def rotation90(keyBumps, edgeLength) :
    
    newKeyBumps = set()
    for keyBump in keyBumps :
        currentRow, currentCol = keyBump
        
        nextCol = edgeLength - 1 - currentRow
        nextRow = currentCol 
        
        newKeyBumps.add((nextRow, nextCol))
        
    return newKeyBumps



