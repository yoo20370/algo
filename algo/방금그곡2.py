# 솔루션 형태로 풀어보자 

def replace(string) :
    return string.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", 'b')

def get_minute(time) :
    hour = int(time[0]) 
    minute = int(time[1])

    return hour * 60 + minute 

def solution(m, musicinfos):
    result_list = []
    m = replace(m)
    
    for musicinfo in musicinfos :
        musicinfo_list = musicinfo.split(",")
        
        # 필요한 데이터 매핑 
        music_name = musicinfo_list[2]
        music_tone_list = musicinfo_list[3]
        music_tone_list = replace(music_tone_list)
        
        # 라디오 음악 재생 시간 
        start_time = get_minute(musicinfo_list[0].split(":"))
        end_time = get_minute(musicinfo_list[1].split(":"))
        
        play_time = end_time - start_time
        
        # 라디오에서 재생된 음악 구하기 
        music_length = len(music_tone_list) 
        
        value = play_time // music_length 
        remain = play_time % music_length
        
        total_tone_list = music_tone_list * value 
        total_tone_list += music_tone_list[:remain]
        
        if m in total_tone_list :
            result_list.append((music_name, play_time))
        
    if len(result_list) == 0 :
        return "(None)"
    else :
        result_list.sort(reverse=True, key=lambda x : x[1])
        return result_list[0][0]
