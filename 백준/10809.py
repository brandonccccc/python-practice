S = str(input())
a = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(a)):
    if a[i] in S:
        print(S.index(a[i]), end=' ')
    else:
        print(-1, end=' ')