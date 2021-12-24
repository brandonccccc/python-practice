from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    q = deque([])
    cnt = 0
    for idx, importance in enumerate(imp):
        q.append([importance, idx])
    while q:
        if q[0][0] != max(imp):
            q.append(q.popleft())
        else:
            if q.popleft()[1] == m:
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
                imp.remove(max(imp))
            