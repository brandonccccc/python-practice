#n, m을 입력받기
n, m = map(int, input().split())

# 2차원 리스트 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 연결 노드 방문하기
def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x >= n or x <= -1 or y >= m or y <= -1:
        return False
    # 현재 노드를 방문하지 않았으면
    if graph[x][y] == 0:
        #방문처리
        graph[x][y] = 1
        # 상하좌우 노드 방문 여부 확인(재귀적 호출)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True: # 이어진 곳의 시작지점(제일 작은 위치)를 카운팅
            result += 1

print(result)