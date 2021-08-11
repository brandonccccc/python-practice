T = int(input())
sum = 1

for _ in range(T):
    x, y = map(int, input().split())
    remained = y - x
    z = 1
    sum = 0
    while remained > sum + z*2:
        sum += z*2
        z += 1
    if sum + z >= remained:
        print(2*z -1)
    else:
        print(2*z)
