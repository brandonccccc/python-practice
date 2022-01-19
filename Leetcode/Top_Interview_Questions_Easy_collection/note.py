def singleNumber(nums):
    answer = 'aacc'
    for i in nums:
        answer = answer ^ i
        print(answer)
    return answer

print(singleNumber("ccac"))