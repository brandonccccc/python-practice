def solution(s):
    s_list = list(map(int, s.split(" ")))
    return "{} {}".format(min(s_list), max(s_list))

print(solution("-1 -2 -3 -4"))  