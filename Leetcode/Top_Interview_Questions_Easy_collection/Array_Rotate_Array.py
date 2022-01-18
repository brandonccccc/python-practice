class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        temp = nums[(-1*k):]
        temp += nums[:(k+1)]
        return temp


print(Solution().rotate([1,2,3,4,5,6,7], 3))