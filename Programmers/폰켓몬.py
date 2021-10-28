def solution(nums):
    a = int(len(nums) / 2)
    b = int(len(set(nums)))
    return min(a, b)
    
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))