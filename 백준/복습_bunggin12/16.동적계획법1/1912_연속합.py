n = int(input())
nums = list(map(int, input().split()))
dp = [-1000 for _ in range(100001)]
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])
print(max(dp))

# dp 리스트를 미리 0으로 만들어버리면 음수일때 틀린다..
# 주어질 숫자의 범위가 -1000<= num <= 1000 이므로 -1001로 초기화 한다.