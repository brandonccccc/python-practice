import math
import sys
A, B = map(int, sys.stdin.readline().split())
gcd = math.gcd(A, B)

print('1'*gcd)