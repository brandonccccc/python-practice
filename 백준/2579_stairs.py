n = int(input())
s = list(int(input()) for _ in range(n))
dp = []

if n <3:
    print(sum(s))
else:
    dp.append(s[0])
    dp.append(s[0]+s[1])
    # 경우의 수에 따른 합을 dp 리스트에 차례로 저장하고 최대값이 되는 값을 맨 끝에 추가
    dp.append(max(s[0]+s[2], s[1]+s[2], dp[1]))
    for i in range(3,n):
        dp.append(max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]))
    # dp 리스트의 맨 뒤에 있는 값을 출력할때 -1 을 쓰면 된다...
    print(dp[-1])