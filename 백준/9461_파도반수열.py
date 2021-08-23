T = int(input())
for _ in range(T):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(input())
    if N < 10:
        print(dp[N-1])
    else:
        for i in range(10, N):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[N-1])