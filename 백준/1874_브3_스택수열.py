import sys
input = sys.stdin.readline

n = int(input())
op = ''
series = []
cnt = 1
temp = True

for _ in range(n):
    num = int(input())
    while cnt <= num:
        series.append(cnt)
        op += '+'
        cnt += 1
    if series[-1] == num:
        series.pop()
        op += '-'
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

