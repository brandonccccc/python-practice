rest = []
a = 1

# 입력받은 값을 42로 나눠서 나머지를 리스트 항목으로 추가
for _ in range(10):
    rest.append(int(input()) % 42)
# 비교를 위해서 숫자 크기대로 나열
rest.sort()

# 리스트 항목의 바로 뒤에 있는 값과 비교해서 다르면 개수 추가
for i in range(9):
    if rest[i] != rest[i+1]:
        a += 1

print(a)
