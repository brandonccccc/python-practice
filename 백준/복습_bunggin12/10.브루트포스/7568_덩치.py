n = int(input())
member = []
grade_list = [1 for _ in range(n)]
for _ in range(n):
    member.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        # 각 항목 전체를 순회하면서 현재 기준에서 키, 몸무게 둘다 크면 1을 더함
        if i != j:
            if member[j][0] > member[i][0] and member[j][1] > member[i][1]:
                grade_list[i] += 1
print(*grade_list)