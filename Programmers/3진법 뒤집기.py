def solution(n):
    num = ''
    
    while n > 0:
        num += str(n%3)
        n = n // 3
    
    return int(num, 3)
    


print(solution(45))
print(solution(125))
