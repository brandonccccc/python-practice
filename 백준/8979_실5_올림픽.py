import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if medals[i][0] == k:
        index = i
for i in range(n):
    if medals[index][1:] == medals[i][1:]:
        print(i+1)
        break
print(medals)