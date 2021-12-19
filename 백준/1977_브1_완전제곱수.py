m = int(input())
n = int(input())
squres = []
answer = []
for i in range(1, 101):
    squres.append(i**2)

for i in squres:
    if i >= m and i <= n:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))