n = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[n])

# 마지막에만 나머지 연산을 해 주는 것이 아니라 for문 안에서도 계속 계산해주어야 한다.
# 그렇ㅈ ㅣ않으면 숫자가 엄청나게 커진다.