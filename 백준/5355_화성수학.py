T = int(input())
for _ in range(T):
    equa = list(input().split())
    ans = float(equa[0])
    for i in range(len(equa)):
        if equa[i] == '@':
           ans = ans * 3
        elif equa[i] == '%':
            ans = ans + 5
        elif equa[i] == '#':
            ans = ans - 7
    print("{:.2f}".format(ans))