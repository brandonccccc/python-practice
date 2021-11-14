def solution(numbers):
    # 문자열 비교를 위해 str로 변환
    numbers = list(map(str, numbers))
    # 조건이 1000이하의 값이므로, x를 3번 반복한 문자열끼리 비교한다.
    # 문자열 비교를 하면 문자열의 첫번째 인덱스 값으로 비교하게 된다.
    # 문자열 비교는 문자의 ASCII 값을 기준으로 정렬하게 되며, 같으면 다음 인덱스의 ASCII값을 비교한다.
    # 오름차순 정렬로 reverse를 해준다.
    numbers.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))