n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    margin = r + c - e
    if margin < 0 :
        print("advertise")
    elif margin == 0:
        print("does not matter")
    else:
        print("do not advertise")