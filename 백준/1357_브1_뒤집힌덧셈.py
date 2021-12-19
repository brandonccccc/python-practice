x, y = map(int, input().split())

def Rev(x):
    x = str(x)[::-1]
    return int(x)

print(Rev(Rev(x) + Rev(y)))