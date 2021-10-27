def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return(len(d))

print(solution([1,3,2,5,4], 9))
print(solution([2, 2, 3, 3], 10))