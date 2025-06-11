# 장르별 재생 횟수를 기록하고 정렬해야 함 -> dic로 만들어서 기록 | 장르 : 누적 재생 수 |
# 장르 내부에서 재생된 노래를 정렬해야 함 -> dic로 만들어서 배열 관리 | 장르 : [(인덱스, 재생수), (인덱스, 재생수)]

def solution(genres, plays):
    
    answer = []
    play_rank = {}
    genres_list = {}
    
    length = len(genres) 
    
    for index in range(length) :
        genre = genres[index]
        play = plays[index]
        
        data = play_rank.get(genre)
        if data :
            play_rank[genre] = data + play
        else :
            play_rank[genre] = play
            
        data = genres_list.get(genre)
        if data :
            data.append([index, play])
        else :
            genres_list[genre] = [[index, play]]
            
    play_rank_list = list(play_rank.items())
    play_rank_list.sort(reverse=True, key = lambda x : x[1])
    
    for genre, play in play_rank_list :
        genre_list = sorted(genres_list.get(genre), key = lambda x : (x[1], -x[0]))
        
        cnt = 0
        while genre_list and cnt < 2 :
            index, play = genre_list.pop()
            answer.append(index)
            cnt += 1
        
    return answer