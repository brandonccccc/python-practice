class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                answer += (prices[i+1] - prices[i])
        return answer

print(Solution().maxProfit([7,1,5,3,6,4]))