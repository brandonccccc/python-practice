def solution(num):
    a = [False, False] + [True]*(num-1)
    primes = []

    for i in range(2, num+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, num+1, i):
                a[j] = False
    return len(primes)

"""

def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i)) # i의 배수들을 뺌
    return len(num)
    
"""

print(set(range(2,11)))
print(set(range(2*2,11,2)))