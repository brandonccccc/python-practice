t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    answer = 1
    for _ in range(n):
        name, part = input().split()
        if part not in clothes:
            clothes[part] = 1
        else: clothes[part] += 1
    for part in clothes:
        answer *= (clothes[part] + 1)
    print(answer-1)
# 해당 파트를 안입는 경우를 포함하기 위해서 +1 을 한 값들을  모두 곱하고,
# 아무것도 안입은 경우를 빼주면 된다.