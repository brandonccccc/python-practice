n, k = map(int, input().split())
cnt = 0

data = [True] * (n+1)
for i in range(2, len(data) + 1):
    for j in range(i, n+1, i):
        if data[j] == True:
            data[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break

# 모든 정수에 대해서 보는 것이므로, index를 값으로 생각할 수 있음
# 공배수여서 이미 없어지는 경우가 있으므로 단순 삭제하는 방법은 사용하면 안됨
