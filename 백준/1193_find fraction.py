X = int(input())
n = 1
a, b = 0, 0
while 1:
    if X - n <= 0:
        if n % 2 == 0:
            a = X
            b = n + 1 - X
            print("{}/{}".format(a, b))
        else:
            a = n + 1 - X
            b = X
            print("{}/{}".format(a, b))
        break
    else:
        X -= n
        n += 1