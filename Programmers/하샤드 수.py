def solution(x):
    return x % sum([int(a) for a in str(x)]) == 0

print(solution(10))

import math
print(math.lcm(3, 12))