T = int(input())
nums = list(map(int, input().split()))
prime = 0
for num in nums:
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        prime += 1
print(prime)

