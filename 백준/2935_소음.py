import sys
input = sys.stdin.readline
a = int(input())
m = list(input())
b = int(input())
if m[0] == '*':
    print(a * b)
elif m[0] == '+':
    print(a + b)