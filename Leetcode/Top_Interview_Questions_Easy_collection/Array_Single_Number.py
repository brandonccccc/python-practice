class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic_nums = {}
        for i in nums:
            if i in dic_nums:
                dic_nums[i] += 1
            else:
                dic_nums[i] = 1
        for k, v in dic_nums.items():
            if v == 1:
                return k

# def singleNumber(nums) -> int:
#     answer = 0
#     for i in nums:
#         answer = answer ^ i
#         print(answer)
#     return answer