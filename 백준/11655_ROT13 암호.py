s = input()
answer = ""

for c in s:
    if 'a'<= c<= 'z':
        answer += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        answer += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        answer += c
    
print(answer)