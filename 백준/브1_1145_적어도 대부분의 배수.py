from math import gcd
from itertools import combinations

nums = list(map(int, input().split()))
answer = list(combinations(nums, 3))

def lcm_n(array):
    def lcm(x, y):
        return x*y // gcd(x,y)

    while True:
        array.append(lcm(array.pop(), array.pop()))
        if len(array) == 1:
            return array[0]

            
for i in range(len(answer)):
    answer[i] = list(answer[i])
    answer[i] = lcm_n(answer[i])

print(min(answer))