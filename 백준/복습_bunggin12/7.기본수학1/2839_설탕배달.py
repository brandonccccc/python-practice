n = int(input())
# dp 를 위한 리스트 생성. n의 범위는 5000으로 나누어 떨어지지 않는 경우를 거르기 위해 범위를 넘어서는 값으로 초기화한다.
# 3~5 까지의 값을 입력했을 때 -1 값을 반환하기 위해 입력값보다 5만큼 더 긴 리스트를 생성한다
sugar = [5001 for _ in range(n+5)]
# 3kg과 5kg일 때의 초기값
sugar[3] = 1
sugar[5] = 1

# 5 초과의 값에 대해서 값을 계산한다.
for i in range(6, n+1):
    # 3칸 전 값과 5칸 전 값을 비교해 더 작은 수에다가 1을 더해나간다.
    # ex) 15의 경우 3칸 전인 12는 3kg짜리 4개, 5칸 전인 10은 5kg짜리 2개로 5kg 1개를 더하면 되므로 3이 된다.
    sugar[i] = (min(sugar[i-3], sugar[i-5]) + 1)

# n번째 값을 출력한다. 해당 값이 5001보다 작으면 해당 값을 출력하고, 크다면(위 조건을 만족하지 못한 경우) -1을 출력한다.
print(sugar[n] if sugar[n] <5001 else -1)