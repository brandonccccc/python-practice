t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    # 순서와 층에 맞도록 a,b 계산
    a = n % h
    b = (n // h) + 1
    # n이 h의 배수일 경우 a는 0이 되므로 h로 바꿔주고 b는 하나가 넘어가버리니까 1을 빼줌
    if a == 0:
        a = h
        b -= 1
    # b가 1자리수 일 경우 a와 b 사이에 0을 넣어줌 (범위가 99까지이므로 2자리 경우까지만 고려해주면 됨)
    if len(str(b)) > 1:
        print(str(a) + str(b))
    else:
        print(str(a) + '0' + str(b))