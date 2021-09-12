import math
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    gcd = []
    for i in range(1, nums[0]+1):
        for j in range(i+1, nums[0]+1):
            gcd.append(math.gcd(nums[i], nums[j]))
    print(sum(gcd))