import sys
input = sys.stdin.readline

n = int(input())
lopes = []
answer = []
for _ in range(n):
    lopes.append(int(input()))

lopes.sort()
for i in range(n):
    answer.append(lopes[i]*(n-i))

print(max(answer))