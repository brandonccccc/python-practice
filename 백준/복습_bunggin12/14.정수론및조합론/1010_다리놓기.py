def factorial(x):
    ans = 1
    while x:
        ans *= x
        x -= 1
    return ans

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = (factorial(m)//factorial(m-n))//factorial(n)
    print(ans)
    
# 팩토리얼을 내장 함수를 안쓰고 직접 계산하니까 시간초과 안나옴