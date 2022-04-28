a, b = map(str, input().split())
print(max(int(a[::-1]), int(b[::-1])))
# 문자열 뒤집는 방법 : [::-1] 하면 된다.
# 문자열로 입력 받고 int(뒤집은 수) 끼리 비교해서 큰 값 출력