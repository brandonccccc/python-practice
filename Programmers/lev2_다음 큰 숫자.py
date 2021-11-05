def solution(n):
    A = list(bin(n))[2:]
    cnt = A.count("1")
    while True:
        n += 1
        B = list(bin(n))[2:]
        if B.count("1") == cnt:
            B = "".join(B)
            return int(B, 2)
        
print(solution(78))
print(solution(15))