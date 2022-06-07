import math
n = int(input())
r_list = list(map(int, input().split()))
for i in range(1, n):
    gcd = math.gcd(r_list[0], r_list[i])
    print(str(r_list[0]//gcd) + '/' + str(r_list[i]//gcd))
