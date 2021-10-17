n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

nums.sort()
print(nums)
count = int(m / (k+1)) * k + m % (k+1)

answer += count * nums[-1]
answer += (m - count) * nums[-2]

print(answer)