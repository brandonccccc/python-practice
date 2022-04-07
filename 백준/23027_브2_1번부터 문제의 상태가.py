s = list(input())

# 1
if 'A' in s:
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == 'C' or s[i] == 'D' or s[i] == 'F':
            s[i] = 'A'

# 2
elif 'A' not in s and 'B' in s:
    for i in range(len(s)):
        if s[i] == 'C' or s[i] == 'D' or s[i] == 'F':
            s[i] = 'B'

# 3
elif 'A' not in s and 'B' not in s and 'C' in s:
    for i in range(len(s)):
        if s[i] == 'D' or s[i] =='F':
            s[i] = 'C'

# 4
elif 'A' not in s and 'B' not in s and 'C' not in s:
    s = 'A' * len(s)
        
print(''.join(s))