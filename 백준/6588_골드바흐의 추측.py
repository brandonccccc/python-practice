r = 1000000
#에라토스테네스의 체
check = [True for _ in range(r)]
for i in range(2, int(r**0.5)+1):
    if check[i] == True:
        for j in range(i*2, r, i):
            if check[j] == True:
                check[j] = False

import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for i in range(3, r+1):
        if check[i] == True:
            if check[N-i] == True:
                print("%d = %d + %d"%(N, i, N-i))
                break