n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda t:t[0])
a.sort(key=lambda t:t[1])
for x,y in a:
    print(x,y)