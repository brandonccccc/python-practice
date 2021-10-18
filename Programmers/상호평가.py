def solution(scores):
    answer = ""
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])
        if s[i] == min(s) and s.count(s[i]) == 1:
            del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1:
            del s[i]
        
        avr = sum(s) / len(s)
        if avr >= 90:
            answer += "A"
        elif avr >= 80:
            answer += "B"
        elif avr >= 70:
            answer += "C"
        elif avr >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer

