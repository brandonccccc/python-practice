x = int(input())
cnt = 1
sum = 1
# 몇번째 대각선에 있는지 cnt에 저장
while sum <= x:
    sum += cnt
    cnt += 1
# 칸 수 전체에서 몇번째 있는지 확인하기 위한 변수 rest
rest = sum - x
# 짝수번째 줄일때와 홀수번째 줄일때 순서가 다름
if cnt % 2 == 0: 
    print(str(rest)+'/'+str(cnt - rest))
else:  
    print(str(cnt-rest)+'/'+str(rest))