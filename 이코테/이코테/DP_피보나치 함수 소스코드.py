"""def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(4))"""

"""import math
import time

# 한번 계산된 결과를 메모이제이션(memoization) 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑 다운 DP)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화실에 따라 계산
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

start = time.time()
print(fibo(99))
end = time.time()
print(f"{end - start:.30f} sec")"""

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])