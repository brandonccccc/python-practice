import sys
N = int(sys.stdin.readline())
ans = 1
if N == 0:
    print(1)
else:
    while True:
        ans *= N
        N -= 1
        if N == 0:
            print(ans)
            break
