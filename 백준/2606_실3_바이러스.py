n = int(input())
node = int(input())
connection = [[]*n for _ in range(n+1)] 
visited = [0] * (n+1)
cnt = 0

for i in range(node):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

def dfs(v):
    global cnt
    visited[v] = 1
    for i in connection[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)

print(cnt)
