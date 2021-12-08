import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p += t
q += t

if (p // w) % 2 == 0:
    p %= w
else:
    p = w - (p%w)

if (q // h) % 2 == 0:
    q %= h
else:
    q = h - (q%h)

print(p, q)