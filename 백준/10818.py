N = int(input())
# N개의 항목을 가진 리스트 생성 (하고 싶은데 안되네)
num1 = [0 for i in range(0, N)]


# 초기화한 리스트에 띄어쓰기로 리스트에 항목 추가
#for i in range(1):
num1 = list(map(int, input().split()))

print(min(num1), max(num1))
