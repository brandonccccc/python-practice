import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
list_num = []

for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            list_num.append(i)

if len(list_num) == 0:
    print(-1)
else:
    print(sum(list_num))
    print(min(list_num))