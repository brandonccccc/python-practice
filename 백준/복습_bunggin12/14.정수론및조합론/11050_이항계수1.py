n, k = map(int, input().split())
def factorial(x):
    ans = 1
    while x:
        ans *= x
        x -= 1
    return ans
print(factorial(n) // (factorial(k) * factorial(n-k)))