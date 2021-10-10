def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = list(s)
    for i in range(len(s)):
        if s[i] in big:
            s[i] = big[(big.index(s[i])+n)%26]
        if s[i] in small:
            s[i] = small[(small.index(s[i])+n)%26]
    return "".join(s)

    
s = "a"
print(solution("a B z", 1))
print((ord(s[0])))

"""
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    
"""