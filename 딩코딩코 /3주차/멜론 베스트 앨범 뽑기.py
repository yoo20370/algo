MX_GENRES = 101

def solution(genres, plays):
    answer = []
    
    genre_plays_count = {}
    sing_info_table = [[] for _ in range(MX_GENRES)]
    
    for index in range(len(genres)) : # O(N)
        genre_name = genres[index]
        play_count = plays[index]
        
        if genre_plays_count.get(genre_name) != None:
            genre_plays_count[genre_name] = genre_plays_count.get(genre_name) + play_count
            
        else : 
            genre_plays_count[genre_name] = play_count
        
        hash_index = hash(genre_name) % MX_GENRES
        sing_info_table[hash_index].append((genre_name, index, play_count))
    
    # items()를 사용하여 딕셔너리를 리스트로 변환 
    genre_plays_count_array = list(genre_plays_count.items())
    # # 딕셔너리 -> 배열로 변환 # O(N )
    # for genre_name in genre_plays_count.keys() : 
    #     value = genre_plays_count.get(genre_name)
    #     genre_plays_count_array.append((genre_name, value))
    
    # 속한 노래가 많이 재생된 장르 정렬 O(NlgN)
    genre_plays_count_array.sort(key=lambda x : -x[1])
    
    # 장르별 정렬 수행 O(100 * NlgN)
    for i in range(MX_GENRES) :
        sing_info_table[i].sort(key=lambda x : (-x[2], x[1]))
    
    # 장르 내에서 많이 재생된 노래를 먼저 수록한다. 최대 2개 
    for genre_name, plays in genre_plays_count_array :
        count = 0
        
        hash_index = hash(genre_name) % MX_GENRES
        
        for name, index, play in sing_info_table[hash_index] :
            if count >= 2 :
                break
            answer.append(index)
            count += 1

    
    return answer

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", solution(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))