class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for i, v in enumerate(nums):
            if target - v in dict_nums:
                return [dict_nums[target-v], i]
            else:
                dict_nums[v] = i

