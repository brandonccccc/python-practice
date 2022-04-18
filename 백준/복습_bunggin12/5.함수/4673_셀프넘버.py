#1~10000까지 모두 들어있는 리스트 생성
nums = [i for i in range(1, 10001)]

for i in range(1, 10001):
    dn = str(i)
    next_dn = i
    for j in dn:
        # 다음 d(n)값을 구하기 위해 d(n)을 str로 바꾸고 각 자리수를 다시 int로 변환해서 더함
        next_dn += int(j)
    # 다음 값이 nums에 들어있으면 삭제
    if next_dn in nums:
        nums.remove(next_dn)

for i in nums:
    print(i)