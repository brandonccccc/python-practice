food = list(map(int, input().split()))
k = int(input())
i = 0

while k != 0:
    if food[i%3] != 0:
        food[i%3] -= 1
        i += 1
        k -= 1
    else:
        i += 1

print(food)
print(i%3)
result = (i%3) + 1
