import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = []


for _ in range(n):
    data.append(int(input()))
data.sort()
cnt = Counter(data).most_common(2)

# 산술평균
print(round(sum(data)/n))
# 중앙값
print(data[n//2])
# 최빈값
if len(data) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(max(data) - min(data))
