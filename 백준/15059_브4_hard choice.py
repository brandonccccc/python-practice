a = list(map(int, input().split()))
r = list(map(int, input().split()))
answer = 0
for i in range(len(a)):
    if a[i] - r[i] < 0:
        answer += (r[i] - a[i])
print(answer)