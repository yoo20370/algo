# 0207 실패 
import sys 

solution_count = int(sys.stdin.readline().rstrip())
solution_list = list(map(int, sys.stdin.readline().split()))

solution_list.sort()


def solution(solution_count, solution_list) -> None :

    alkali_solution_index = 0
    acidity_solution_index = solution_count - 1
    min_offset = int(1e10)
    min_alkali_solution = 0
    min_acidity_solution = 0

    while solution_list[alkali_solution_index] < 0 and solution_list[acidity_solution_index] > 0 :
    # while alkali_solution_index != acidity_solution_index :

        two_solution_sum = solution_list[alkali_solution_index] + solution_list[acidity_solution_index]

        if min_offset > abs(0 - two_solution_sum) :
            min_offset = abs(0 - two_solution_sum)
            print(min_offset, two_solution_sum, solution_list[alkali_solution_index], solution_list[acidity_solution_index], abs(0 - two_solution_sum))
            min_alkali_solution = solution_list[alkali_solution_index]
            min_acidity_solution = solution_list[acidity_solution_index]

        if two_solution_sum == 0 :
            min_alkali_solution = solution_list[alkali_solution_index]
            min_acidity_solution = solution_list[acidity_solution_index]
            break
        
        elif two_solution_sum < 0 :
            alkali_solution_index += 1

        else :
            acidity_solution_index -= 1
    
    print(min_alkali_solution, min_acidity_solution)

solution(solution_count, solution_list)