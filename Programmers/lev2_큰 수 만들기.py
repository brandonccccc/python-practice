def solution(number, k):
    answer = [] #stack
    for num in number:
        if not answer: #answer가 비어 있으면
            answer.append(num) #첫 숫자를 넣는거
            continue
        if k > 0:
            while answer[-1] < num: #answer의 마지막 숫자가 이번 숫자보다 작으면
                answer.pop() #작은 숫자는 제거
                k -= 1 #횟수 1회 줄이기
                if not answer or k <= 0: #k가 0이 되면
                    break 
        answer.append(num)
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))