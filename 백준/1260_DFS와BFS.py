import sys
read = sys.stdin.readline
from collections import deque

N, M, V = map(int, read().split())
graph = [[0] * (N +1) for i in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, read().split())
    # 노드연결
    graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색(BFS)
def bfs(start_v):
    discovered = [start_v]
    # 리스트를 써서 pop(0) 하면 O(N) 이다.
    # 시간복잡도가 O(1)인 deque 사용
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[V][w] == 1 and (w not in discovered):
                discovered.append(w)
                queue.append(w)
    
 # 깊이 우선 탐색
def dfs(start_v, discoverd=[]):
  discoverd.append(start_v)
  print(start_v, end=' ')

  for w in range(len(graph[start_v])):
    if graph[start_v][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)

dfs(V)
print()
bfs(V)
