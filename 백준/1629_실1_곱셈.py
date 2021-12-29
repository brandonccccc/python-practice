a, b, c = map(int, input().split())

def DaC(a, b):
    if b == 1:
        return a % c
    
    temp = DaC(a, b//2)
    
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c
    
print(DaC(a, b))

"""
분할정복
지수가 짝수이면 예를 들어 10^10 = 10^5 * 10^5 로 표현 가능
지수가 홀수이면 예를 들어 10^11 = 10^5 * 10^5 * 10 으로 표현
정해진 값을 절반으로 나눠서 계산
"""