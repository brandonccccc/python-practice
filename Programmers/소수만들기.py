def solution(nums):
    # 툴로 3개 선택한 튜플로 구성된 리스트 생성하고 각 튜플 더하기
    from itertools import combinations
    com = list(combinations(nums, 3))
    for i in range(len(com)):
        com[i] = sum(com[i])
    
    # ㅔ라토스테네스의 채 로 소수 리스트 만들어 둠
    n = 3000
    a = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
                    
    cnt = 0                
    for num in com:
        if num in primes:
            cnt += 1
    
    return cnt


print(solution([1,2,3,4]))