A, B, C = map(int, input().split())
for _ in range(1):
    if C == B:
        print(-1)
        break
    elif A/(C-B) < 0:
        print(-1)
    else:
        print(int((A/(C-B))+1))