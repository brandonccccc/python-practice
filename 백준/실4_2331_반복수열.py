a, p = map(int, input().split())
def num_cal(num, p):
    num_list = [int(i) for i in str(num)]
    ans = 0
    for i in range(len(num_list)):
        ans += num_list[i] ** p
    return ans

nums = [a]

while True:
    nums.append(num_cal(nums[-1], p))
    if nums[-1] in nums[:-2]:
        print(nums.index(nums[-1]))
        break

