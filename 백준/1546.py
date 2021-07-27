
# 평균 계산을 위한 과목 개수 입력
N = int(input())
# 점수 입력 받아서 score 리스트에 항목으로 입력
score = list(map(int, input().split()))
# score 리스트에서 최고 점수 찾아내 M을 초기화
M = max(score)

# score 리스트의 항목을 새로 계산한 값으로 변환
for i in range(len(score)):
    score[i] = (score[i]/M)*100

# score 리스트 값을 다 더해서 새로운 평균 구하여 출력
print(sum(score)/N)
