def solution(msg):
    answer = []
    dict = {}
    w, c = 0, 0
    for i in range(26):
        dict[chr(65+i)] = i + 1

    while True:
        c += 1
        if c == len(msg):
            answer.append(dict[msg[w:c]])
            break
        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = len(dict) + 1
            answer.append(dict[msg[w:c]])
            w = c
        
    return answer


print(solution('KAKAO'))