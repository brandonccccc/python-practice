from itertools import product
s1, s2, s3 = map(int, input().split())
dices = [[i for i in range(1,s1+1)], [i for i in range(1,s2+1)], [i for i in range(1,s3+1)]]
prod = list(product(*dices))
for i in range(len(prod)):
    prod[i] = sum(prod[i])

d = dict()

for num in prod:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

answer = [key for key, value in d.items() if max(d.values()) == value ]

print(min(answer))