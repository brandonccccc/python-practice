n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]
dp[1] = wine[0]
dp[2] = wine[0] + wine[1]

for i in range(3, n+1):
    