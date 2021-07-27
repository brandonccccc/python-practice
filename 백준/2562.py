# 입력받을 리스트 초기화
num = []
# num 리스트에 차례로 입력하기 (enter 쳐서 리스트의 맨 뒤에 추가)
for i in range(1, 10):
    number = int(input())
    num.append(number)
print(max(num))
# num 리스트의 맥시멈 값의 인덱스에다가 1을 더해서 출력 (인덱스는 0부터 시작하니까)
print(num.index(max(num))+1)
