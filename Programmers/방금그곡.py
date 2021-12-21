# 두 문자로 된 경우를 다른 문자로 치환한다 (아래의 경우 대문자+#을 소문자로 치환)
def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    

    return music_ 
def solution(m, musicinfos):
    m = changecode(m)
    answer = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = changecode(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
