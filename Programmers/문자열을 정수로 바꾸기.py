def solution(s):
    if s[0] == "+":
        return int(s[::1])
    elif s[0] == "-":
        return int(s)
    else:
        return int(s)

print(solution(str(+1234)))