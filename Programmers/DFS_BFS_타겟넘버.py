def solution(numbers, target):
    answer = 0
    q = [[numbers[0],0], [-1*numbers[0], 0]]
    while q:
        num, idx = q.pop()
        idx += 1
        if idx < len(numbers):
            q.append([num+numbers[idx], idx])
            q.append([num-numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    return answer

print(solution([1,1,1,1,1], 3))