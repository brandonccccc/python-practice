"""N = int(input())
for i in range (1, N+1):
    print(i)"""

N = int(input())
a = []
for i in range(1,N+1):
    a.append(i)

for i in range(1,N+1):
    print(a[N-i])