while True:
    a, b, c = map(int, input().split())
    # a, b, c 가 크기 순으로 들어온다는 조건이 없으므로 크기 순으로 정렬하여 계산
    abc = sorted(list([a, b, c]))
    if a == b == c == 0:
        break
    else:
        if abc[0]**2 + abc[1]**2 == abc[2]**2:
            print('right')
        else:
            print('wrong')