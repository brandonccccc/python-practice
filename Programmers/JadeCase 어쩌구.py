def solution(s):
    s_list = list(s)
    if s_list[0].isalpha():
        s_list[0] = s_list[0].upper()
    for i in range(1, len(s_list)):
        if s_list[i-1] == " " and s_list[i].isalpha():
            s_list[i] = s_list[i].upper()
        else:
            s_list[i] = s_list[i].lower()
    return "".join(s_list)
            

print(solution("3people unFollowed me"))