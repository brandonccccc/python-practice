n = int(input())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
for i in nums:
    print(i, end=' ')