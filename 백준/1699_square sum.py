N = int(input())
cnt = 0

while 1:
    a = int(N**(1/2))
    if a**2 <= N < (a+1)**2:
        N -= a**2
        cnt += 1
    if N == 0:
        print(cnt)
        break
