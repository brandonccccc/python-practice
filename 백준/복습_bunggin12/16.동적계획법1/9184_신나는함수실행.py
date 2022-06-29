def w(a, b, c):
    if a<=0 or b<=0 or c<=0: return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if dp[a][b][c] : return dp[a][b][c]
    
    elif a<b and b<c :
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))


# 점화식이 있을 때, 어떻게 DP로 표현하느냐를 알려주는 문제이다.
# 변수가 3개 이므로 각각 경우에 대한 리스트를 전부 만들어주면 된다..!;
# 모든수가 20 이상의 경우는 통일되어 있으므로 DP 리스트는 21까지 초기화해 둔다.
