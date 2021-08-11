T = int(input())



for j in range(T):
    n = int(input())
    d = [0, 1, 2, 4]
    for i in range(4, n+1):
        d.append(d[i-1] + d[i-2] + d[i-3])
    print(d[n])