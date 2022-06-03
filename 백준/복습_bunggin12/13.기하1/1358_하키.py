w, h, x, y, p = map(int, input().split())
r = h/2
cnt = 0
for _ in range(p):
    xp, yp = map(int, input().split())
    if x <= xp <= x+w and y <= yp <= y+h:
        cnt += 1
    elif r >= ((xp-x)**2 + ((yp-(r+y))**2))**0.5 :
        cnt += 1
    elif r >= ((xp-(w+x))**2 + ((yp-(r+y))**2))**0.5:
        cnt += 1
print(cnt)