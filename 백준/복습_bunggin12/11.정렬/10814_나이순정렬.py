import sys
input = sys.stdin.readline

n = int(input())
members = []
for _ in range(n):
    members.append(list(input().split()))
members.sort(key = lambda x: int(x[0]))
for i in members:
    print(*i)