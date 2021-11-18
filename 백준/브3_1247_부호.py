import sys
input = sys.stdin.readline
n1 = int(input())
a1 = 0
for i in range(n1):
    a1 += int(input())
if a1 == 0:
    print(0)
elif a1 < 0:
    print('-')
else:
    print('+')

n2 = int(input())
a2 = 0
for i in range(n2):
    a2 += int(input())
if a2 == 0:
    print(0)
elif a2 < 0:
    print('-')
else:
    print('+')

n3 = int(input())
a3 = 0
for i in range(n3):
    a3 += int(input())
if a3 == 0:
    print(0)
elif a3 < 0:
    print('-')
else:
    print('+')