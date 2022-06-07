import math

n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort()
interval = []
ans = []
for i in range(1, n):
    interval.append(nums[i] - nums[i-1])

prev = interval[0]
for i in range(1, len(interval)):
    prev = math.gcd(prev, interval[i])
    
for i in range(2, int(prev**0.5)+1):
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)
ans = list(set(ans))
ans.sort()
print(*ans)

"""for i in range(2, min(nums)+1):
    remains = [nums[j] % i for j in range(n)]
    if remains.count(remains[0]) == n:
        print(i, end = ' ')""" # 시간 초과..
        
