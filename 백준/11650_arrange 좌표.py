n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda t:t[1])
a.sort(key=lambda t:t[0])
for x,y in a:
    print(x,y)