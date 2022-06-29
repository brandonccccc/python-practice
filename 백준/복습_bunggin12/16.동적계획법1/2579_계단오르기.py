n = int(input())
stair = [0 for _ in range(n+3)]
for i in range(n):
    stair[i] = int(input())
dp = [0 for _ in range(n+3)]
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3]+stair[i-1] + stair[i])
print(dp[n-1])

# 조건에서 n의 범위가 300이하 라고만 했으므로, 1일때와 2일때에도 처리를 해줘야한다.
# 처음 코드를 짰을때 1,2 인 경우에 처리를 할 수 없었어서 인덱스 에러가 났었다.
# stair와 dp를 초기화 할떄 미리 301개씩 해버리는거도 괜찮을듯