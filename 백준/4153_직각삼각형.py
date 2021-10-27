while True:
    lenth = list(map(int,input().split()))
    lenth.sort()
    if lenth[0] == 0 and lenth[1] == 0 and lenth[2] == 0:
        break
    if lenth[0]**2 + lenth[1]**2 == lenth[2]**2:
        print("right")
    else:
        print("wrong")