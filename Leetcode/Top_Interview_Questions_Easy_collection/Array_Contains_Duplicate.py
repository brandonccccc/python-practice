class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            temp = dic.get(nums[i], 2) # nums[i] 가 있으면 value를, 없으면 디폴트 지정한 2 를 가져옴
            if temp != 2:
                return True
            dic[nums[i]] = 1 # 값을 넣어둠으로써 다음 싸이클에서 디폴트가 아닌 값을 가져온다면 True
        return False

print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))

