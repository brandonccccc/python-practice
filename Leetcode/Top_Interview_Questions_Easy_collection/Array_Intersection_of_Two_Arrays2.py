class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer = []
        for i in nums2:
            if i in nums1:
                nums1.remove(i)
                answer.append(i)
        return answer