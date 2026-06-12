# 멜론 베스트 앨범 

# 속한 노래가 많이 재생된 장르를 먼저 수록 -> 장르별 재생 횟수를 기록해서 순위를 만들어야 함  
# 장르 내에서 많이 재생된 노래를 먼저 수록 -> 장르별 노래 재생 횟수 순위를 기록해야함 
# 장르별 노래 재생 횟수 순위 정렬시 고유번호를 두 번째 정렬 기준으로 잡는다. 

def solution(genres, plays):
    
    length = len(genres)
    
    genreRank = {}
    genrePlayRank = {}
    
    for index in range(length) :
        genre = genres[index]
        play = plays[index]
        
        if genreRank.get(genre) is None :
            genreRank[genre] = play
            
        else :
            value = genreRank.get(genre) 
            genreRank[genre] = value + play
    
        if genrePlayRank.get(genre) is None :
            # (재생횟수, 고유번호) 
            genrePlayRank[genre] = [(play, index)]
        
        else :
            genrePlayRank[genre].append((play, index))
    
    genreRankList = list(genreRank.items())
    genreRankSortedList = sorted(genreRankList, key=lambda x : x[1], reverse=True)
    
    answer = []
    for index in range(len(genreRankSortedList)) :
        genreName, playCount = genreRankSortedList[index]
    
        genrePlaySortedRank = sorted(genrePlayRank[genreName],reverse=True, key = lambda x : (x[0], -x[1] ))
        
        songIndex = 0 
        count = 0 
        
        while songIndex < len(genrePlaySortedRank) and count < 2 :
            playCount, number = genrePlaySortedRank[songIndex]
            answer.append(number) 
            songIndex += 1
            count += 1
        
    return answer