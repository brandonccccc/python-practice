def isPrimenum(n):
    err = 0
    # 어떤 수를 i로 나눠가면서 나눠지는 값이 있으면 err에 값을 더함
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            err += 1
    # 값의 제곱근까지의 값 중에 나눠지는 값이 없으면 소수이고 err값이 0이다.
    if err == 0:
        return n

prime_nums = []
for i in range(2, 1001):
    if isPrimenum(i) != None: prime_nums.append(isPrimenum(i))

n = int(input())
nums_input = list(map(int, input().split()))
cnt = 0
for num in nums_input:
    if num in prime_nums: cnt+= 1

print(cnt)