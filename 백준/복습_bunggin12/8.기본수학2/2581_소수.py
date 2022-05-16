def isPrimenum(n):
    err = 0
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            err += 1
    if err == 0:
        return n

prime_nums = []

m, n = int(input()), int(input())
if m == 1 : m = 2
for i in range(m, n+1):
    if isPrimenum(i) != None: prime_nums.append(isPrimenum(i))

if len(prime_nums) == 0:
    print(-1)
else:
    print(sum(prime_nums))
    print(min(prime_nums))