n = int(input())
for i in range(1, n+1):
    divide_sum = []
    for j in str(i):
        divide_sum.append(int(j))
    if n == i + sum(divide_sum):
        print(i)
        break
    if n == i:
        print(0)