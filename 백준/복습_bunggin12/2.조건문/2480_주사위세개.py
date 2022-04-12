a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a != b and b != c and a != c:
    print(max(a,b,c) * 100)
elif a == b != c or a == c != b:
    print(a*100 + 1000)
elif b == c != a:
    print(b*100 + 1000)
    