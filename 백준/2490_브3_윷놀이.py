for _ in range(3):
    s = list(map(int, input().rstrip().split()))
    state = s.count(0)
    if state == 1:
        print("A")
    elif state == 2:
        print("B")
    elif state == 3:
        print("C")
    elif state == 4:
        print("D")
    else:
        print("E")