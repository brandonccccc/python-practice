import sys
N, K = map(int, sys.stdin.readline().split())
circle = [i+1 for i in range(N)]
ans =[]
i = 0
for _ in range(N):
    i += K-1
    if i >= len(circle):
        i = i % len(circle)

    ans.append(str(circle.pop(i)))


print("<", ", ".join(ans),">", sep='')