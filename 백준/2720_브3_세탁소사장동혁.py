# 그리디, 거스름돈 문제와 동일

# 받을 횟수 입력
case = int(input())
q, d, ni, p = 0, 0, 0, 0

for _ in range(case):
    n = int(input())
    q = n // 25
    n %= 25
    d = n // 10
    n %= 10
    ni = n // 5
    n %= 5
    p = n
    print(q, d, ni, p)


