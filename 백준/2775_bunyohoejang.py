T = int(input())
apart = [[0] * 15 for _ in range(15)]
for i in range(15):
    apart[0][i] = i

for _ in range(T):
    k = int(input())
    n = int(input())

    for a in range(k+1):
        for b in range(n+1):
            if apart[a][b] == 0:
                for c in range(b+1):
                    apart[a][b] += apart[a-1][c]

    if apart[k][n] != 0:
        print(apart[k][n])
