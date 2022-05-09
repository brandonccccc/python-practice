n = int(input())
cnt = 1
sum = 1
# 벌집이 그려지는 칸의 총 수를 더해가면서 더한 값이 입력값보다 커지면 끝
while sum < n:
    sum += 6*cnt
    cnt += 1
print(cnt)