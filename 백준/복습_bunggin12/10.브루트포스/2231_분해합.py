n = int(input())
divi_sum = []

for i in range(n):
    sum_i = 0
    # 각 자리수 더하기
    for j in range(len(str(i))):
        sum_i += int(str(i)[j])
    # 각 자리수와 지금 수 더하기
    divsum = sum_i + i
    # 분해합을 입력한 값과 비교하여 같으면 리스트에 추가
    if divsum == n:
        divi_sum.append(i)
        
# 분해합 리스트가 비어있으면 0 출력, 있으면 최소값 출력
if len(divi_sum) == 0: print(0)
else : print(min(divi_sum))