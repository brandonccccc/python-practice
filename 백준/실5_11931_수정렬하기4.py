import sys
nums = sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True)
for i in range(len(nums)):
    print(nums[i])
