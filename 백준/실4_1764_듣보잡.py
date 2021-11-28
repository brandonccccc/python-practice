import sys
input = sys.stdin.readline

a = []
b = []
n, m = map(int, input().split())
for _ in range(n):
    a.append(input().rstrip())
for _ in range(m):
    b.append(input().rstrip())

c = set(a) & set(b)

print(len(c))
for i in sorted(c):
    print(i)
