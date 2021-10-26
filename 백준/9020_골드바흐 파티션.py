def isPrime(num):
    if num == 1: 
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: 
            return False
    return True

li = list(range(2,10000))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(N):
        if prime_li[i] > N:
            tmp = prime_li[:i]
            print(tmp)
        if prime_li[i] == True:
            if prime_li[N-i] == True:
                print("%d = %d + %d"%(N, i, N-i))
                break