def isPrimenum(n):
    if n == 1: return False
    else: 
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

# 입력하는 값마다 소수의 개수를 구하면 시간초과가 난다.
# 주어진 범위 전체 내에 있는 소수를 모두 구해서 리스트로 저장한다.
prime_nums = []
for i in range(1, 123456*2 + 1):
    if isPrimenum(i) : prime_nums.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0 : break
    # 미리 구한 리스트에서 n보다 크고 2n보다 같거나 작은 값들의 개수를 세면 끝
    for i in prime_nums:
        if i > n and i <= 2*n:
            cnt += 1
    print(cnt)