n = int(input())
cnt_fib = 0
cnt_fibonacci = 0
"""def fib(n):
    global cnt_fib
    if n==1 or n==2: return 1
    else: 
        cnt_fib += 1
        return fib(n-1) + fib(n-2)"""

def fibonacci(n):
    global cnt_fibonacci
    f = [0 for _ in range(41)]
    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt_fibonacci += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

print(fibonacci(n), cnt_fibonacci)

# 첫번째 코드는 하나하나 계산하는 코드기 때문에 두번째 코드의 n번째 값을 출력해주면 된다.
# 몇 번 도는지 확인하기 위해 cnt변수를 global로 선언하고 for문이 돌때마다 1씩 더한다.
# 나는 index 0에서의 값을 0으로 그냥 뒀기때문에 리스트 f의 길이를 41까지 해야 범위를 벗어나지 않는다.
