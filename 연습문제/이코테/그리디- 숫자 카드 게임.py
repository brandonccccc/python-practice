n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
answer = []
for i in range(n):
    answer.append(min(nums[i]))
print(max(answer))