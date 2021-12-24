from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    k = int(nums[0])
    nums = nums[1:]
    if k == 0:
        break
    answer = list(combinations(nums, 6))
    for i in answer:
        print(*i)
    print()