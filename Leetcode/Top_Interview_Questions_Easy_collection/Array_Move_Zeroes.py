class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            # print(nums)
            # print(zero)
        return nums

    # Two Pointer
    # one is for iterating list 
    # anoter is for zero number.(record index of zero)

print(Solution().moveZeroes([0,1,0,3,12]))