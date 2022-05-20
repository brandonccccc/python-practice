n = int(input())
cnt = 0
# 첫번째 숫자 666 부터 시작
ans = 666
while True:
    # 666이 증가하는 수 ans에 포함되어 있으면 카운트 증가
    if '666' in str(ans):
        cnt += 1
        # 카운트가 n 과 같을 때 ans 출력
        if n == cnt:
            print(ans)
            break
    # 위 조건을 만족하지 않으면 증가하는 수 ans는 1씩 증가
    ans += 1
