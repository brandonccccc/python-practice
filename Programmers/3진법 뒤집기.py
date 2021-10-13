def solution(n):
    num = ''
    
    while n > 0:
        num += str(n%3)
        n = n // 3
    # 여기서 num을 뒤집어야 실제 n진수가 나옴. 이번 문제는 뒤집기이기 떄문에 따로 처리하지 않음
    return int(num, 3)
    


print(solution(45))
print(solution(125))
