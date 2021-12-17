def solution(n):
    money = [500, 100, 50, 10]
    answer = 0
    for coin in money:
        answer += n // coin
        n = n % coin
    return answer

print(solution(1260))