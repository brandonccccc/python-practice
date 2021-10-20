n = int(input())
nums = list(map(int, input().split()))
cnt_num = 0
for i in range(n):
    cnt = 0
    if nums[i] > 1:
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                cnt += 1
        if cnt == 0:
            cnt_num += 1

print(cnt_num)