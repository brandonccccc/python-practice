# 테스트 케이스 개수
C = int(input())

for _ in range(0, C):
    # 개수, 점수 입력 받음
    score = list(map(int, input().split()))
    # 개수, 점수 리스트 분리
    N = score[0]
    score = score[1:]
    # 합과 평균 구해서 초기화
    sum1 = int(sum(score))
    avr = sum1 / N
    # score의 항목 중 avr보다 큰 값을 항목으로 가지는 c1 리스트 초기화
    c1 = [x for x in score if x > avr]
    # float, 소수점 3자리까지. 평균 이상 리스트 c1의 갯수가 score에 입력된 항목 개수기준 비율을 구하여 출력
    print("{:.3f}%".format(100*len(c1)/(len(score))))
