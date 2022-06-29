s = 'abcd'
print(s) 

for i in range(len(s)):
    if s[i] == 'b':
        s[i] = 'c'

print(s)