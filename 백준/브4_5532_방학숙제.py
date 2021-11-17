import math
a = [0, 0, 0, 0, 0]

for i in range(5):
    a[i] = int(input())
b = a[1] / a[3]
c =  a[2] / a[4]

print(a[0] - max(math.ceil(b), math.ceil(c)))