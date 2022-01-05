import sys
input = sys.stdin.readline
# 1<=n<=100, 1<=k<=10,000, 동전 가치는 100,000보다 작거나 같다
n, k = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(n)]
# 가능한 값/불가능한 값 판별을 위해서 범위를 벗어나는 큰 값으로 기본 설정
dp = [10001 for i in range(k+1)]
dp[0] = 0  # k범위를 넘는 0은 0으로 처리
# 각 코인값에 대해서
for i in coins:
    # 코인 값 ~ 마지막까지 +1씩 하면서 처리
    for j in range(i, k+1):
        # 현재값에서 가져온 코인 값을 빼줬을때 코인 사용개수에 지금 코인 개수 하나를 더한값과 
        # 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교하여 더 작은값을 넣는다.
        dp[j] = min(dp[j], dp[j-i] + 1)

# 값 k가 위 for문에서 바뀌지 않고 그대로 10001이 들어있다면 불가능한 값이므로 -1 출력
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
