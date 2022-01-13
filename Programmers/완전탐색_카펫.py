def solution(brown, yellow):
    total = brown + yellow
    for i in range(int(total/2), 2, -1):
        if total % i == 0:
            if ((i + total//i)-2) * 2 == brown:
                return [i, total//i]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))