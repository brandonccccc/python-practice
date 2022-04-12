score = int(input())
if score >= 90: print('A')
elif score >= 80: print('B')
elif score >= 70: print('C')
elif score >= 60: print('D')
else: print('F')

# 윗 범위에서 점수가 걸리면 먼저 출력되기 때문에 굳이 범위로 표현할 필요가 없었다.