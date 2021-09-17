import sys
N = int(sys.stdin.readline())
ans = 1
if N == 0:
    ans = 1
else:
    while True:
        ans *= N
        N -= 1
        if N == 0:
            break

count = 0
ans = str(ans)[::-1]
for i in range(len(ans)+1):
    if ans[i] == '0':
        count += 1
    if ans[i] != '0':
        print(count)
        break