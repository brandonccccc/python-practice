T = int(input())
a = []
b = []

for i in range (1, T+1):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

for i in range(0, T):
    print("Case #"+format(i+1)+": " + format(a[i]+b[i]))