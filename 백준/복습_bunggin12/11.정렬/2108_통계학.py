from collections import Counter
import sys
input = sys.stdin.readline

def modefind(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

avr = round(sum(nums) / n)
center_num = nums[n//2]
modes = modefind(nums)
range_nums = max(nums) - min(nums)

print(avr)
print(center_num)
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])
print(range_nums)