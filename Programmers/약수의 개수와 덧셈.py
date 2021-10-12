def solution(left, right):
    answer = []
    
    for i in range(left, right+1):
        cnt = 0
        # 약수의 갯수 구하기
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer.append(i)
        else:
            answer.append(i * -1)
    return sum(answer)