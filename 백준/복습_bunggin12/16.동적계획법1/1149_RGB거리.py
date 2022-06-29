# 조건
# 1번집의 색은 2번 집의 색과 같지 않아야 한다.
# N번집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 <= i <= N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야한다.
# 즉 같은 색이 연속으로 나타나면 안된다.

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
    
for i in range(1,n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][1], cost[i-1][0])
print(min(cost[n-1]))

# 각 색깔별로 시작해서 그 색을 제외하고 다른 색 중 싼거만 계속 더해나간다
