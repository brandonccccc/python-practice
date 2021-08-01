T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    b = (N // H) + 1
    if a == 0:
        a = H
        b = N//H
    print('%d%02d' %(a,b))
