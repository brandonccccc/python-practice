import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = [list(map(int, input().rstrip().split())) for _ in range(2)]
    for j in range(1, n):
        # index 1에서 시작하면 윗줄에서는 왼쪽 아래꺼를 선택할 수 있고, 
        # index 2에서는 왼아래 대각선꺼를 취할지, 그 전 대각선것을 취할지 max로 판별해서 더해나간다.
        if j == 1:
            s[0][j] += s[1][j-1]
            s[1][j] += s[0][j-1]
        else:
            s[0][j] += max(s[1][j-1], s[1][j-2])
            s[1][j] += max(s[0][j-1], s[0][j-2])
    print(max(s[0][n-1], s[1][n-1]))
