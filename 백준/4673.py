n = 1
list1 = []

# 원래 숫자와 각 자리수의 숫자를 더하는 함수 선언
def addnumber(n):
    s = str(n)
    x = n
    for i in s:
        x += int(i)
    return x

# 1~10000까지 addnumber 함수 돌린 수를 다 저장한 리스트 생성
for i in range(10001):
    addnumber(i)
    if addnumber(i) <= 10000:
        list1.append(addnumber(i))

# 생성된 list1을 순서대로 정리하고 set(집합으로 선언)하여 중복 숫자 삭제
list1.sort()
list1 = set(list1)

# 1~10000까지 없으면 출력
for i in range(1, 10001):
    if i in list1:
        continue
    else:
        print(i)
