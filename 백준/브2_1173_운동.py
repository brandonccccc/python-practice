N, m, M, T, R = map(int, input().split())
time_rest = 0
time_exce = 0
h = m

if h + T > M:
        print(-1)
else:
    while time_exce < N:
        if h + T > M:
            h -= R
            if h < m:
                h = m
            time_rest += 1
        elif h + T <= M:
            h += T
            time_exce += 1

    print(time_rest + time_exce)