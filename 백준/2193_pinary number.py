N = int(input())

dp = [[0]*2 for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 0



for i in range(2, N+1):
    for j in range(2):
        if j == 0:
            dp[i][j] = dp[i-1][0] + dp[i-1][1]
        elif j == 1:
            dp[i][j] = dp[i-1][0]
            
print(sum(dp[N-1]))