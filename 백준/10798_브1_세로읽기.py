s = [str(input()) for i in range(5)]
answer = ''

for i in range(len(s)):
    if len(s[i]) < 15:
        s[i] = s[i] + ' '* (15 - len(s[i]))
for i in range(15):
    for j in range(5):
        answer += s[j][i]
answer = answer.replace(' ', '')
print(answer)