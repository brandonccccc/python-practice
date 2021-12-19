"""from itertools import combinations
def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans

name = str(input())
n = int(input())
answer = {}

for _ in range(n):
    team_name = str(input())
    cnt = []
    for i in range(len(name)):
        cnt.append(team_name.count(name[i])+1)
    cnt = list(combinations(cnt,2))
    cnt = [sum(cnt[i]) for i in range(len(cnt))]
    answer[team_name] = cnt

answer = dict(sorted(answer.items()))
print(answer)
print(max(answer, key = answer.get))"""


ms = input()
n = int(input())
li = sorted([input() for i in range(n)])
max_p = max_i = 0
for i in range(n):
    L = ms.count("L") + li[i].count("L")
    O = ms.count("O") + li[i].count("O")
    V = ms.count("V") + li[i].count("V")
    E = ms.count("E") + li[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_p < p:
        max_p = p
        max_i = i
print(li[max_i])