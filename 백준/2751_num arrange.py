N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())
a.sort()
for i in range(N):
    print(a[i])