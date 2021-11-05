def solution(n):
    cnt = 0
    for i in range(1, n+1):
        num = 0
        while num < n:
            num += i
            i += 1
            if num == n:
                cnt += 1
    return cnt

print(solution(15))