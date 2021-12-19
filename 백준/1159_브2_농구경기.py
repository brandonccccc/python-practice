n = int(input())
names = []
for i in range(n):
    names.append(input()[0])

    
d = dict()

for letter in names:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

answer = [key for key, value in d.items() if value >= 5]
answer.sort()


if len(answer) >= 1:
    for i in range(len(answer)):
        print(answer[i], end='')
else:
    print("PREDAJA")