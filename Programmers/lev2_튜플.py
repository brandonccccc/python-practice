def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    s_list.sort(key = len)
    for i in s_list:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))