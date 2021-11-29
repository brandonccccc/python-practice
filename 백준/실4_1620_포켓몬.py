import sys
input = sys.stdin.readline

n, m = map(int, input().split())
monsters = {}
monsters2 = []

for i in range(n):
    name = input().rstrip()
    monsters[name] = i+1
    monsters2.append(name)
    

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(monsters2[int(a)-1])
    else:
        print(monsters[a])
