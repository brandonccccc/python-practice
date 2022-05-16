#에라토스테네스의 채

def isPrimenum(n):
    if n == 1: return False
    else: 
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

m, n = map(int, input().split())
for i in range(m, n+1):
    if isPrimenum(i):
        print(i)
