n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1
arry = []
for i in range(n):
    arry.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn = 0
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and arry[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        if arry[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(cnt)
