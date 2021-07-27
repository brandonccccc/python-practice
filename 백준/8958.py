# 테스트 케이스 입력 횟수
N = int(input())
# 입력한 횟수만큼 반복
for _ in range(0, N):
    # 답을 입력, O/X를 리스트로 저장
    answer = list(map(str, input().upper()))
    # 정답마다 점수를 입력할 리스트 선언
    score = []
    # 답을 입력한 리스트의 항목 갯수만큼 반복해서 항목에 따른 점수를 매기고 score 리스트에 각 항목의 점수를 입력
    for i in range(0, len(answer)):
        # 첫번째가 O일 경우 앞의 값이 없기때문에 1을 먼저 받기 위해서 조건문 사용
        if answer[i] == 'O':
            # i번째 항목이 O인데 앞이랑 같으면 1을 더한 값을 score에 저장
            if i >= 1 and answer[i] == answer[i-1]:
                score.append(int(score[i-1]) + 1)
            else:
                score.append(1)
        elif answer[i] == 'X':
            score.append(0)
    print(sum(score))
