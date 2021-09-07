# (가 나오면 1을 더하고, )가 나오믄 1을 뺀다.
# 순서대로 하다가 -1이 되면 이미 짝이 안맞으니까 NO에 break
# 다 끝나고 0이면 딱 맞는거고 1 이상이면 짝이 안맞는거
import sys
T = int(input())
for _ in range(T):
    a = sys.stdin.readline()
    s = list(a)
    sum = 0
    for i in s:
        if i == '(':
           sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
            