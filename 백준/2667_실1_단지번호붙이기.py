import sys
input = sys.stdin.readline

n = int(input())
villa = []
for _ in range(n):
    villa.append(list(map(int, input().rstrip())))
cnt = 0
num = []

def dfs(x, y):
    global cnt
    if x>=n or x <= -1 or y >= n or y <= -1:
        return False
    if villa[x][y] == 1:
        global cnt
        cnt += 1
        villa[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])