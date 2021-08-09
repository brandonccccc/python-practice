x, y = map(int, input().split())
#x월 y일이 2007년의 몇 번째 날인지 계산한 후 7로 나눠서 요일 알아내기

# 딕셔너리에 월별 날짜 저장, 몇번째 날인지 계산을 위한 date 초기화
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 
         10:31, 11:30, 12:31}
date = 0

#입력된 x에 대해서 딕셔너리에서 x까지의 밸류값을 모두 더하고 y값도 더함
for i in range(1, x):
    date += month[i]
date += y

# 7로 나눠서 요일 알아내기
if date % 7 == 1:
    print('MON')
elif date % 7 == 2:
    print('TUE')
elif date % 7 == 3:
    print('WED')
elif date % 7 == 4:
    print('THU')
elif date % 7 == 5:
    print('FRI')
elif date % 7 == 6:
    print('SAT')
else:
    print('SUN')