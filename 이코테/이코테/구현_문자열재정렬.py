s = input() # s의 길이 1<= s <= 10,000
alph = ''
num = []

s = sorted(s)

for i in range(len(s)):
    if ord(s[i]) >= 65 :
        alph += s[i]
    else:
        num.append(int(s[i]))

print(alph+str(sum(num)))