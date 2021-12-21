import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)
    cnt = 0
    def dfs(v):
        global cnt
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == 0:
                dfs(i)
                cnt += 1
    dfs(1)
    print(cnt)

