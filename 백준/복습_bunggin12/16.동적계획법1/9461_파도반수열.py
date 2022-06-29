t = int(input())
dp = [0 for _ in range(101)]
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
dp[6] = 3
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    n = int(input())
    print(dp[n])

#점화식만 구하면 끝