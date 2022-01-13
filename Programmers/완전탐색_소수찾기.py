from itertools import permutations
def is_prime_number(x):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    nums = []
    for i in range(1, len(num_list)+1):
        temp = list(map(''.join, permutations(num_list, i)))
        nums += temp
    nums = list(map(int, nums))
    nums = list(set(nums))
    
    for i in nums:
        if i > 1 and is_prime_number(i):
            answer += 1

    return answer

print(solution("17"))
print(solution("110"))