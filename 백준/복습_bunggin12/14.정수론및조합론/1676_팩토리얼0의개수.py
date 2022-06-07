def factorial(x):
    result = 1
    while x:
        result *= x
        x -= 1
    return result

n = int(input())
fac_n = str(factorial(n))
cnt = 0
for i in range(len(fac_n)-1, 0, -1):
    if fac_n[i] != '0': break
    else: cnt += 1
print(cnt)