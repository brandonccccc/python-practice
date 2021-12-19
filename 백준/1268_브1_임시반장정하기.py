n = int(input())
answer = [[0]*n for _ in range(n)]
student = [list(map(int, input().split())) for _ in range(n)]

for i in range(5):
    grade = []
    for j in range(n):
        grade.append(student[j][i])
    for j in range(n):
        if grade.count(grade[j]) >= 1:
            for k in range(n):
                if grade[j] == grade[k] and k != j:
                    answer[j][k] = 1
    
li = [sum(student) for student in answer]

print(li.index(max(li))+1)