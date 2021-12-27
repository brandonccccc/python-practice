prime_nums = [0 for i in range(10001)]
prime_nums[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime_nums[j] = 1

t = int(input())
for _ in range(t):
    n = int(input())
    mid = n // 2
    for j in range(mid, 1, -1):
        if prime_nums[n - j] == 0 and prime_nums[j] == 0:
            print(j, n-j)
            break