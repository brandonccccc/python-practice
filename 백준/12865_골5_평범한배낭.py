import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
bag = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]
bag = [[0, 0]] + bag

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    
print(bag)
print(dp)
print(dp[n][k])