N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
a.sort()
for i in range(N):
    print(a[i])