def check_hansoo(num):
    num_list = list(map(int, str(num)))
    if len(num_list) > 1:
        # 0번째, 1번째 빼서 등차수열의 공차 구해둠
        d0 = num_list[0] - num_list[1]
        # 숫자 길이 만큼 각 자리값을 빼가면서 비교, 틀리면 멈추고 다음 i로 넘어감
        for i in range(1, len(num_list)):
            if d0 != (num_list[i-1] - num_list[i]):
                break
        else: return num
    
hansoo_list = []
n = int(input())
for i in range(1, n+1):
    if i < 10:
        hansoo_list.append(i)
    if check_hansoo(i) != None:
        hansoo_list.append(check_hansoo(i))
    
print(len(hansoo_list))


# 다른 사람 풀이==========================================
"""def hansoo(num):
    hansoo_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int, str(i)))
        if i < 100:  # 100보다 작으면 모두 한수
            hansoo_cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            # 주어진 범위가 1000보다 작거나 같은 자연수이고 1000은 한수가 아니므로
            # 위와 같이 0,1 뺀 값, 1,2 뺀 값만 비교하면 된다.
            hansoo_cnt += 1
    return hansoo_cnt
n = int(input())
print(hansoo(n))"""