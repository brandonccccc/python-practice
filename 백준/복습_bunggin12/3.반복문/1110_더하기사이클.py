n = input()
# 입력한 n이 한자리수이면 앞에 0을 붙임
if len(n) == 1:
    n = '0' + n
# 새로운 수를 업데이트하기 위한 값 선언(처음엔 n과 같도록, 나중에 n과 비교할 값)
a = n
# 몇 번이 지나야 돌아오는지 확인하기 위한 카운트
cnt = 0
while True:
    cnt += 1
    # 업데이트된 새로운 값 a의 각 자리수를 더하고 한자리수, 두자리수 에 따라 다르게 처리
    tmp = str(int(a[0]) + int(a[1]))
    if len(tmp) == 2:
        a = a[1] + tmp[1]
    else:
        a = a[1] + tmp
    # 처음 입력한 n과 같은 값이 되면 카운트를 출력하고 while문 중단    
    if a == n : 
        print(cnt) 
        break
    
# 문제에 주어진대로 그대로 코딩함 ㅋㅋ