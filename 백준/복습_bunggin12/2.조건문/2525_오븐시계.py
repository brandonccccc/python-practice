a, b = map(int, input().split())
c = int(input())

# 주어진 시간을 60으로 나눠서 몫은 시간, 나머지는 분으로 a, b 에 더함
a += c//60
b += c%60

# 더한 값이 시간 조건을 넘어서면 맞춰서 값을 업데이트
if b >= 60:
    a += 1
    b -= 60
if a > 23:
    a -= 24

print(a, b)