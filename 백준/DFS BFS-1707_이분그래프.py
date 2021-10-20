import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(now, group):
    #현재 노드를 방문 처리
    vis[now] = group
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in arr[now]:
        # 안가본 노드면 방문
        if vis[i] == 0:
            if not dfs(i, -group):
                return False
        # 방문한 곳인데 색이 다르면 취소
        elif vis[i] == vis[now]:
            return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    vis = [0] * (v+1)
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    ans = True
    for i in range(1, v+1):
        if vis[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    print("YES" if ans else "NO")