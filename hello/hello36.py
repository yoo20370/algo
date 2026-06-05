
def solution(genres, plays):
    answer = []
    
    musicCount = len(genres)
    
    genreRank = {}
    genrePlayRank = {}
    
    for index in range(musicCount) :
        # 장르 Rank 만들어야 함 - genreRank { name : play}
        # 장르별 Rank 만들어야 함 - musicRank { name :[[index, play]]}
        
        genre = genres[index]
        play = plays[index]
        
        if genreRank.get(genre) :
            playCount = genreRank.get(genre)
            genreRank[genre] = playCount + play
        else :
            genreRank[genre] = play
        
        if genrePlayRank.get(genre) :
            genrePlayRank.get(genre).append([index, play])
        
        else :
            genrePlayRank[genre] = [[index, play]]
        
        
    genreRankList = sorted(list(genreRank.items()), reverse = True, key = lambda x : x[1])
    
    for genre, play in genreRankList : 
        
        genrePlayRankList = sorted( genrePlayRank[genre], reverse=True, key = lambda x : (x[1], -x[0]))
        maxIndex = 0
        rankIndex = 0
        
        while rankIndex < len(genrePlayRankList) and maxIndex < 2 :
            answer.append(genrePlayRankList[rankIndex][0])
            maxIndex += 1
            rankIndex += 1
    
    return answer