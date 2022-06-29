n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            
print(sum(dp[n])%1000000000)

# 자리수가 늘어날 때 마다 몇개씩 늘어나는지 세어보고 점화식으로 적용해보려 했으나, 경우의 수가 계속 늘어나서 점화식으로 표현하기는 힘들다.
# 어떤한 자리에서 각 숫자(0~9) 위치에서 나타나는 수의 개수로 dp를 계산해 나간다. (2차원)
# 