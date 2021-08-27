def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2-1:len(s)//2+1]        
    else:
        return s[len(s)//2]


"""def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]"""