def solution(answers):
    answer = []
    score = [0, 0, 0]
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a1[i % 5] == answers[i]:
            score[0] += 1
        if a2[i % 8] == answers[i]:
            score[1] += 1
        if a3[i % 10] == answers[i]:
            score[2] += 1
    maxim = max(score)
    for i in range(len(score)):
        if score[i] == maxim:
            answer.append(i+1)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))