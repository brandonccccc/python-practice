from itertools import combinations
n, s = map(int, input().split())
series = list(map(int, input().split()))
all = []

for i in range(1, n+1):
    temp = list(combinations(series, i))
    all = all + temp
for i in range(len(all)):
    all[i] = list(all[i])
    all[i] = sum(all[i])

print(all.count(s))