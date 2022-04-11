a, b = int(input()), int(input())

# b의 각 자리수를 값으로 가져오기 위해서 tmp에 b를 저장하고 10으로 나눈 나머지를 가져오고 몫으로 업데이트
# 3번 반복하면 각 자리수를 변수로 저장할 수 있다.
tmp = b
b1 = tmp % 10
tmp = tmp // 10
b10 = tmp % 10
tmp = tmp // 10
b100 = tmp


print(a*b1)
print(a*b10)
print(a*b100)
print(a*b)