class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = list(map(str, digits))
        return list(str(int(''.join(digits)) + 1))