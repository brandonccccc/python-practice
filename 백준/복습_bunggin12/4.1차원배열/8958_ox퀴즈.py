t = int(input())
for _ in range(t):
    ans = list(input())
    # 하나 앞의 수와 비교를 하려면 for문을 두번째 항 부터 돌려야 하므로 맨 앞거는 미리 바꿔둠
    if ans[0] == 'O':
        ans[0] = 1
    else: ans[0] = 0
    for i in range(1, len(ans)):
        if ans[i] == 'O':
            ans[i] = ans[i-1] + 1
        elif ans[i] == 'X':
            ans[i] = 0
    print(sum(ans))
    
# 'O'면 그냥 1 더하면됨. 앞 값이 'X'면 0으로 바뀌기 때문에
# 'O'로 다시 시작되는 구간에서 1을 더하면서 1로 시작하게 됨