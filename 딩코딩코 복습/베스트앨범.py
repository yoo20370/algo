# 속한 노래가 많이 재생된 장르를 먼저 수록 
# 장르 내에서 많이 재생된 노래를 먼저 수록 
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록 

# 장르별 plays 수를 계산한다. [장르, 카운트]
# 장르별 정렬 -> (재생수, 고유번호) 형태로 원소를 저장한다. 

# 장르별 plays를 정렬한다. 
# 각 장르가 저장된 배열을 돌면서 최대 2개까지 출력한다. 
 
def get_melon_best_album(genre_array, play_array):
    
    result = []

    geners = {}
    geners_plays = {}

    for index in range(len(genre_array)) :
        genre = genre_array[index] 
        play = play_array[index]

        plays = geners.get(genre)
        # 장르별 plays 개수 카운트 
        if plays == None :
            geners[genre] = play
            geners_plays[genre] = []
            geners_plays[genre].append((play, index))

        else :
            geners[genre] = plays + play
            geners_plays[genre].append((play, index))
    
    
    geners = list(geners.items())
    geners.sort(key=lambda x : x[1])

    while geners :
        genre, plays = geners.pop()

        geners_list = geners_plays.get(genre)
        geners_list.sort(key=lambda x : (x[0], -x[1]))
        
        for i in range(2) :
            if geners_list :
                play, index = geners_list.pop()
                result.append(index)        

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))



# MX_GENRES = 101

# def solution(genres, plays):
#     answer = []
    
#     genre_plays_count = {}
#     sing_info_table = [ [] for _ in range(MX_GENRES)]
    
#     for index in range(len(genres)) : # O(N)
#         genre_name = genres[index]
#         play_count = plays[index]
        
#         if genre_plays_count.get(genre_name) != None:
#             genre_plays_count[genre_name] = genre_plays_count.get(genre_name) + play_count
            
#         else : 
#             genre_plays_count[genre_name] = play_count
        
#         hash_index = hash(genre_name) % MX_GENRES
#         sing_info_table[hash_index].append((genre_name, index, play_count))
    
#     genre_plays_count_array = []
#     # 딕셔너리 -> 배열로 변환 
#     for genre_name in genre_plays_count.keys() : # O(N)
#         value = genre_plays_count.get(genre_name)
#         genre_plays_count_array.append((genre_name, value))
    
#     # 속한 노래가 많이 재생된 장르 정렬 O(NlgN)
#     genre_plays_count_array.sort(key=lambda x : -x[1])
    
#     # 장르별 정렬 수행 O(100 * NlgN)
#     for i in range(MX_GENRES) :
#         sing_info_table[i].sort(key=lambda x : (-x[2], x[1]))
    
#     # 장르 내에서 많이 재생된 노래를 먼저 수록한다. 최대 2개 
#     for genre_name, plays in genre_plays_count_array :
#         count = 0
        
#         hash_index = hash(genre_name) % MX_GENRES
        
#         for name, index, play in sing_info_table[hash_index] :
#             if count >= 2 :
#                 break
#             answer.append(index)
#             count += 1

    
#     return answer