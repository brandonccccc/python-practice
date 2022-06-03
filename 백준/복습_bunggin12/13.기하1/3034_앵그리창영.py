n, w, h = map(int, input().split())
maxim = int((w*w + h*h) ** 0.5)
for i in range(n):
    match = int(input())
    if match > maxim: print('NE')
    else: print('DA')