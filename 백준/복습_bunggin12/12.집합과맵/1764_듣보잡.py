import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dudbo = {}
ans = []
# n번, m번 중 듣보잡 이름은 두번 반복되기때문에 합쳐서 입력받아도 된다.
for _ in range(n+m):
    name = input().rstrip()
    if name not in dudbo:
        dudbo[name] = 1
    else:
        dudbo[name] += 1
# 딕셔너리 정렬 방법
dudbo = dict(sorted(dudbo.items()))

for name in dudbo:
    if dudbo[name] == 2:
        ans.append(name)
print(len(ans))
for n in ans:
    print(n)