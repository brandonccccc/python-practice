# n진법 변환 함수
def convert(n, base):
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer_list = ''
    answer = ''
    for i in range(m*t):
        answer_list += convert(i, n)
    for i in range(t):
        if m*i > m*t or len(answer) == t:
            break
        answer += answer_list[m*i+(p-1)]
    return answer

print(solution(16, 16, 2, 2))