t = int(input())
def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//GCD(a,b))