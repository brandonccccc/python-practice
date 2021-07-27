N, X = map(int, input().split())
a = [0 for i in range(0, N)]
#길이가 정해진 list 만드는 방법?
#현재 코드는 N 입력과 상관없이 입력하는 수 만큼 리스트가 지정됨...
for _ in range(1):
    a = list(map(int, input().split()))

for i in range(0, len(a)):
    if a[i] < X:
        print(a[i], end=' ')
