N = int(input())
n = 0
if N ==1:
    print(1)
else:
    while 1:
        if N - 6*n -1 <= 0:
            print(n+1)
            break
        else:
            N -= 6*n
            n += 1
