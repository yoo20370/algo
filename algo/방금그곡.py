# 생각나는대로 풀었기 때문에 비효율적이고 코드가 복잡함 

# 재생된 시간이 음악 길이보다 길다면  재생된 시간 > 음악 길이 
# -> 음악이 끊김 없이 처음부터 반복 재생 

# 재생된 시간이 음악 길이보다 짧다면 재생된 시간 < 음악 길이
# -> 처음부터 재생시간만큼만 재생 
    
# 내가 풀려는 방법 
# 1. 우선 m을 명확하게 리스트로 분리한다.
# 2. m의 길이를 구한다. (m은 멜로디)
# 3. musicinfos에서 재생 시간을 구하고,주어진 악보를 이용해 재생된 음 리스트를 만든다.
# 4. 재생된 음 리스트에 내가 들은 음 리스트가 포함되어있는지 확인하고, 있으면 결과 리스트에 음악제목과, 플레이 시간을 넣는다.
# 5. 결과 리스트에 결과가 여러 개인 경우 정렬을 수행하고 재생 시간이 같은 경우 앞의 것을 반환한다. (sort는 제자리 정렬이므로 앞의 것을 반환하면 됨)

from collections import deque 

# 12:00 형태로 매개변수 전달 받아야 함 
def get_minute(input_time) :
    time = input_time.split(":")
    hour = int(time[0])
    minute = int(time[1])
        
    return (hour * 60) + minute 

def change_tone_list(music) :
    tone_list = []
    
    queue = deque(list(music))
    
    while queue :
        curr_tone = queue.popleft()
        
        if queue and queue[0] == "#" :
            curr_tone += queue.popleft()
            
        tone_list.append(curr_tone)

    return tone_list
            

def solution(m, musicinfos):
    
    tone_list = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
    # 어떻게 할거임 ?? 
    # 일단, 음악의 길이를 구한다.
    
    play_list = []
    for musicinfo in musicinfos :
        musicinfo_list = musicinfo.split(",")
        
        # 재생된 시간 구하기 
        start_time = get_minute(musicinfo_list[0])
        end_time = get_minute(musicinfo_list[1])
        
        play_time = end_time - start_time
        
        # 재생된 음악 이름, 악보 
        music_name = musicinfo_list[2]
        music = musicinfo_list[3]
        
        # 악보를 리스트로 바꾸고, 음악 재생 시간(이 음악은 몇 분짜리 음악인지) 
        music_tone_list = change_tone_list(music)
        music_play_time = len(music_tone_list)
        
        # 전체적으로 재생된 악보를 생성 
        total_music_play_tone = []
        minute = 0 
        while minute < play_time :
            index = minute % music_play_time
            total_music_play_tone.append(music_tone_list[index])
            minute += 1 
        
        melody = change_tone_list(m)
        melody_time = len(melody)

            
        for index in range(play_time - melody_time + 1) :
            a = total_music_play_tone[index: index + melody_time]
              
            if a == melody :
                play_list.append((music_name, play_time))

    
    if len(play_list) == 0 :
        return "(None)"
    else : 
        play_list.sort(reverse=True, key=lambda x : x[1])
        return play_list[0][0]