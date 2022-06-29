n = int(input())
num_tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(num_tri[i])):
        if j == 0:  # 맨 앞에 있는 수의 경우
            num_tri[i][j] += num_tri[i-1][j]
        elif i == j:  # 맨 뒤에 있는 수의 경우
            num_tri[i][j] += num_tri[i-1][j-1]
        else:  # 그 외의 경우
            num_tri[i][j] += max(num_tri[i-1][j-1], num_tri[i-1][j])

# 각 줄의 인덱스를 생각해서 어느 위치의 값을 더해주는지 잘 생각해봐야한다.

print(max(num_tri[n-1]))