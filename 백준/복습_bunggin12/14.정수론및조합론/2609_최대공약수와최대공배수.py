a, b = map(int, input().split())

def GCD(x, y): # 유클리드 호제법
    while y:
        x, y = y, x%y
    return x

gcd = GCD(a,b)

print(gcd)
print((a*b)//gcd)