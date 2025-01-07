import sys, heapq

INF = int(1e9)

col, row = map(int, sys.stdin.readline().split())

miro = list()

for _ in range(row) :
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

def algo_spot() -> None :
    
    distance = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_cost = [[INF] * col for i in range(row)]

    heap = list()

    heapq.heappush(heap,(miro[0][0], 0, 0))
    min_cost[0][0] = 0

    while heap :
        curr_cost, curr_r, curr_c = heapq.heappop(heap)

        while min_cost[curr_r][curr_c] < curr_cost :
            continue

        for d_r, d_c in distance :
            n_r = d_r + curr_r
            n_c = d_c + curr_c 

            if n_r >= 0 and n_r < row and n_c >= 0 and n_c < col :
                cost = curr_cost + miro[n_r][n_c] 
                if min_cost[n_r][n_c] > cost :
                    min_cost[n_r][n_c] = cost
                    heapq.heappush(heap, (cost, n_r, n_c))

    print(min_cost[row-1][col-1])

algo_spot()
