N = int(input())
a = []
sum1 = 0

for i in range(0, N):
    a.append(i+1)
    sum1 = sum1 + a[i]


print(sum1)