import calendar

def solution(a, b):
    date = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    answer = date[calendar.weekday(2016,a,b)]

    return answer


print(solution(5,24))


#datetime, calendar
