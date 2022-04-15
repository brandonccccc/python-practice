c = int(input())
for _ in range(c):
    n_score = list(map(int, input().split()))
    avg = sum(n_score[1:]) / n_score[0]
    cnt = 0
    for i in n_score[1:]:
        if i > avg : cnt += 1
    print("{:.3f}%".format((cnt/n_score[0])*100))

# 출력문 소수점 제한 방법
# "{.3f}".format(값) : 3부분에 숫자에 따라서 소수점 자리수가 정해짐
# round(값, 자리수) : 자리수까지 출력(자리수+1 에서 반올림)
"""이번 문제에서는 3번쨰 자리까지 출력해야해서 round를 쓸 경우
딱 떨어지는 값에 대해서 오답처리가 된다. 따라서 format을 사용했다. """

