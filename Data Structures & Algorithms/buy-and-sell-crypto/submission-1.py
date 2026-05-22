class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        low, high = 0, 1
        while high < len(prices):
            if prices[high] < prices[low]:
                low = high
            else:
                currentMax = max(prices[high] - prices[low],currentMax)
            high += 1
        return currentMax