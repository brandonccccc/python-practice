t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    # 두 점을 동시에 포함하지 않으면서 각 점을 포함하고 있는 원의 개수를 구하면 될듯?
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        # 점 간의 거리가 r 보다 작으면 포함한다.
        d1 = ((x1-cx)**2 + (y1-cy)**2) ** 0.5
        d2 = ((x2-cx)**2 + (y2-cy)**2) ** 0.5
        # 주어진 원이 d1, d2를 동시에 포함하지 않는 경우 continue
        if d1 >= r and d2 >= r: continue
        # 주어진 원이 d1, d2를 동시에 포함하는 경우도 continue
        elif d1 < r and d2 < r: continue
        else: cnt += 1
    print(cnt)
