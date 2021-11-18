n = list(map(int, input()))


for i in range(1, len(n)):
    mul1, mul2 = 1, 1
    for num in n[:i]:
        mul1 *= int(num)
    for num in n[i:]:
        mul2 *= int(num)
    if mul1 == mul2:
        print("YES")
        break
else:
    print("NO")