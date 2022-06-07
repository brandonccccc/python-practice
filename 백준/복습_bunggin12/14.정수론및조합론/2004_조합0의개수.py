"""n, k = map(int, input().split())
def factorial(x):
    ans = 1
    while x:
        ans *= x
        x -= 1
    return ans
combi = str(factorial(n) // (factorial(k) * factorial(n-k)))
cnt = 0
for i in range(len(combi)-1, 0, -1):
    if combi[i] != '0': break
    else: cnt += 1
print(cnt)"""  # 범위가 200만까지라서 시간초과 남

# 2워 5의 개수를 구하고, 공식으로 10의 개수를 찾아낸다
n, k = map(int, input().split())
def count_two(x):
    two = 0
    while x != 0:
        x //= 2
        two += x
    return two

def count_five(x):
    five = 0
    while x != 0:
        x //= 5
        five += x
    return five

print(min(count_two(n)-count_two(n-k)-count_two(k), count_five(n)-count_five(n-k)-count_five(k)))