import sys
input = sys.stdin.readline
A, B = map(str, input().split())
a, b = 0, 0
for i in range(len(A)):
    a += int(A[i])
for i in range(len(B)):
    b += int(B[i])
print(a*b)
