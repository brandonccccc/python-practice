# A,B,C 입력받음
A = int(input())
B = int(input())
C = int(input())
i = 0
#A,B,C 범위 조건 만족시 실행
while 100<=A<1000 and 100<=B<1000 and 100<=C<1000:
    multiple = A*B*C
    multiple = list(map(int,str(multiple))) # 숫자를 리스트에 항목으로 추가
    for i in range(0, 10):
        print(multiple.count(i))
        i += 1
    # while 문을 빠져나가기 위한 조건문
    if i==10:
        break
