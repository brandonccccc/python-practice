h, w = map(int, input().split())
n = int(input())
a = [[[0] * w] * h]


for i in range(n) :
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(y, y+l) :
        if d == 0:
            a[x][j] = 1
    for j in range(x, x+l):
        if d == 1:
            a[j][y] = 1

                
for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()