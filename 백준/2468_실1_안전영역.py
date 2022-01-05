import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# dfs 정의
# 상하 좌우 에 대해서, 
def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 경계 내에 있고, 아직 방문하지 않았고, 현재 설정된 수면 높이(h) 보다 큰 값에 대하여
        if 0<= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
            #방문처리, 상하좌우 확인
            visited[nx][ny] = True
            dfs(nx, ny, h)
            

n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

ans = 1
# dfs를 높이 별로 수행하기 위해 반복문 추가
for k in range(max(map(max, graph))):
    #각 높이에 대하여 확인해야 하므로 시작 전에 방문 여부, 안전지대 갯수 초기화
    visited = [[False] * n for _ in range(n)]
    safe = 0
    #dfs 수행
    for i in range(n):
        for j in range(n):
            # 지역이 설정된 높이(k)보다 높은 지역이고 방문하지 않았다면
            if graph[i][j] > k and not visited[i][j]:
                # 안전지대 개수 추가 및 방문처리
                safe += 1
                visited[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)
    
print(ans)