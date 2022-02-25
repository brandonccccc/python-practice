import sys
input = sys.stdin.readline

s = list(map(int, input().rstrip()))
len_s = len(s)
dp = [0 for _ in range(len_s+1)]

if s[0] == 0: print(0)
else:
    s = [0] + s 
    dp[0] = dp[1] = 1
    for i in range(2, len_s + 1):
        if s[i] > 0:
            dp[i] += dp[i-1]
        temp = s[i-1]*10 + s[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp[len_s] % 1000000)