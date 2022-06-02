import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_str = set([input() for _ in range(n)])
cnt = 0

for _ in range(m):
    t = input()
    if t in n_str:
        cnt += 1
print(cnt)