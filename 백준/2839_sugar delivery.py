N = int(input())
i = 0
j = 0
ans = -1

for i in range(0, N):
    for j in range(0, N):
        if 5*i + 3*j == N:
            ans = i + j

print(ans)
